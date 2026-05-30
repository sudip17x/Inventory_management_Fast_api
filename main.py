from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import database_models
from database import SessionLocal, engine
from models import Product

try:
    database_models.Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"Warning: Could not create tables: {e}")

app = FastAPI()

# CORS for React dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(f"Database error: {e}")
        raise
    finally:
        db.close()


# list of products with 4 products like phones, laptops, pens, tables
products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

product = Product(id=5, name="Chair", description="A comfortable chair", price=89.99, quantity=15)




def init_db():
    try:
        db = SessionLocal()
        existing_count = db.query(database_models.Product).count()

        if existing_count == 0:
            for product in products:
                db.add(database_models.Product(**product.model_dump()))
            db.commit()
            print("Database initialized with sample products.")
        
        db.close()
    except Exception as e:
        print(f"Database initialization failed: {e}")
        print("Please ensure MySQL is running and accessible at localhost:3306")

init_db()    

@app.get("/products/")
def get_all_products(db: Session = Depends(get_db)):
    try:
        products = db.query(database_models.Product).all()
        return products
    except Exception as e:
        raise HTTPException(status_code=503, detail="Database unavailable. Please ensure MySQL is running and the 'inventory_db' database exists.")


@app.get("/products/{product_id}")
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    try:
        product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
        if product:
            return product
        return {"error": "Product not found"}
    except Exception as e:
        raise HTTPException(status_code=503, detail="Database unavailable. Please ensure MySQL is running and the 'inventory_db' database exists.")

@app.post("/products/")
def create_product(product: Product, db: Session = Depends(get_db)):
    try:
        db.add(database_models.Product(**product.model_dump()))
        db.commit()
        return {"message": "Product created successfully", "product": product}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=503, detail="Database unavailable. Please ensure MySQL is running and the 'inventory_db' database exists.")

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product, db: Session = Depends(get_db)):
    try:
        db_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
        if not db_product:
            raise HTTPException(status_code=404, detail="Product not found")
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        db.refresh(db_product)
        return {"message": "Product updated successfully", "product": db_product}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=503, detail="Database unavailable. Please ensure MySQL is running and the 'inventory_db' database exists.")


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    try:
        db_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
        if not db_product:
            raise HTTPException(status_code=404, detail="Product not found")
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=503, detail="Database unavailable. Please ensure MySQL is running and the 'inventory_db' database exists.")
