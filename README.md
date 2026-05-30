
# FastAPI + React Inventory Management System

A full-stack web application for managing product inventory with a FastAPI backend and React frontend.

## Overview

This project is a complete inventory management system featuring:
- **Backend:** FastAPI REST API with SQLAlchemy ORM and MySQL database
- **Frontend:** React single-page application with product management UI
- **Database:** MySQL for persistent product storage
- **Architecture:** RESTful API design with CORS support for local development

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | FastAPI, SQLAlchemy, PyMySQL |
| Frontend | React, JavaScript |
| Database | MySQL 8.0+ |
| API Format | REST (JSON) |

## Features

✅ View all products with details  
✅ Add new products to inventory  
✅ Update existing product information  
✅ Delete products from inventory  
✅ Real-time API documentation (Swagger UI)  
✅ CORS enabled for frontend integration  
✅ Error handling with meaningful HTTP status codes  

## Backend Implementation Details

### Technology Stack
- **Framework:** FastAPI (Python)
- **ORM:** SQLAlchemy
- **Database:** MySQL (`inventory_db`)
- **Database Driver:** PyMySQL
- **Server:** Uvicorn ASGI server

### Project Structure
```
├── main.py                # FastAPI app with route handlers
├── database.py            # MySQL connection & session factory
├── database_models.py     # SQLAlchemy ORM models
├── models.py              # Pydantic request/response models
└── README.md              # Documentation
```

### Database Models
**Products Table:**
```sql
CREATE TABLE products (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description VARCHAR(500),
  price FLOAT NOT NULL,
  quantity INT NOT NULL
);
```

### API Endpoints

#### Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products/` | Retrieve all products |
| GET | `/products/{product_id}` | Get product by ID |
| POST | `/products/` | Create new product |
| PUT | `/products/{product_id}` | Update product |
| DELETE | `/products/{product_id}` | Delete product |

### Sample API Response
```json
[
  {
    "id": 1,
    "name": "Phone",
    "description": "A smartphone",
    "price": 699.99,
    "quantity": 50
  },
  {
    "id": 2,
    "name": "Laptop",
    "description": "A powerful laptop",
    "price": 999.99,
    "quantity": 30
  }
]
```

### Error Handling
- **404 Not Found:** Product doesn't exist
- **503 Service Unavailable:** Database connection failed
- Returns detailed error messages in JSON format

## Frontend Implementation Details

### Technology Stack
- **Framework:** React 18+
- **Language:** JavaScript (ES6+)
- **Build Tool:** Create React App
- **Backend Integration:** Fetch API for HTTP requests

### Project Structure
```
frontend/
├── public/
│   ├── index.html         # HTML entry point
│   └── manifest.json      # PWA manifest
├── src/
│   ├── App.js             # Main React component
│   ├── App.css            # App styling
│   ├── index.js           # React DOM render
│   ├── index.css          # Global styles
│   ├── TaglineSection.js  # Tagline component
│   └── TaglineSection.css # Tagline styling
└── package.json           # Dependencies & scripts
```

### Features
- Product listing with real-time API data
- Add/edit/delete products via forms
- Responsive design
- Error notifications for failed operations

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14+ & npm
- MySQL 8.0+ (running on localhost:3306)

### Backend Setup

1. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1  # Windows
   source .venv/bin/activate   # macOS/Linux
   ```

2. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn sqlalchemy pymysql
   ```

3. **Create MySQL database:**
   ```bash
   mysql -u root -p
   > CREATE DATABASE inventory_db;
   ```

4. **Update database credentials in `database.py` if needed:**
   ```python
   db_url = "mysql+pymysql://root:password@localhost:3306/inventory_db"
   ```

5. **Start FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```
   - API runs at: `http://localhost:8000`
   - Swagger docs: `http://localhost:8000/docs`

### Frontend Setup

1. **Install dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Start React development server:**
   ```bash
   npm start
   ```
   - App runs at: `http://localhost:3000`
   - Automatically opens in browser

## API Usage Examples

### Get all products
```bash
curl -X GET http://localhost:8000/products/ \
  -H "Content-Type: application/json"
```

### Get product by ID
```bash
curl -X GET http://localhost:8000/products/1 \
  -H "Content-Type: application/json"
```

### Create new product
```bash
curl -X POST http://localhost:8000/products/ \
  -H "Content-Type: application/json" \
  -d '{
    "id": 5,
    "name": "Monitor",
    "description": "27 inch 4K display",
    "price": 399.99,
    "quantity": 15
  }'
```

### Update product
```bash
curl -X PUT http://localhost:8000/products/1 \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "name": "iPhone 15",
    "description": "Latest smartphone",
    "price": 799.99,
    "quantity": 25
  }'
```

### Delete product
```bash
curl -X DELETE http://localhost:8000/products/1 \
  -H "Content-Type: application/json"
```

## Configuration

### Database Connection
Edit `database.py` to change MySQL credentials:
```python
db_url = "mysql+pymysql://username:password@host:port/database_name"
```

### CORS Settings
Frontend origin is configured in `main.py`:
```python
allow_origins=["http://localhost:3000"]
```
Modify this to allow other origins in production.

## Troubleshooting

### Database Connection Errors
- Ensure MySQL is running: `mysql -u root -p`
- Verify `inventory_db` database exists
- Check credentials in `database.py`

### VARCHAR Length Error
- MySQL requires VARCHAR length specifications
- This is handled in `database_models.py` with `String(100)` and `String(500)`

### CORS Errors
- Frontend must be running on `http://localhost:3000`
- Backend CORS is configured to allow this origin

### Port Already in Use
- FastAPI: Change port with `uvicorn main:app --reload --port 8001`
- React: Change port with `PORT=3001 npm start`

## Development Workflow

1. **Start FastAPI backend:**
   ```bash
   uvicorn main:app --reload
   ```

2. **In another terminal, start React:**
   ```bash
   cd frontend
   npm start
   ```

3. **Access the application:**
   - Frontend: `http://localhost:3000`
   - API Docs: `http://localhost:8000/docs`

## Production Deployment

### Backend
- Use production ASGI server (Gunicorn/Uvicorn)
- Set `--reload` to False
- Configure real database credentials
- Update CORS origins
- Use environment variables for secrets

### Frontend
- Build for production: `npm run build`
- Deploy to static hosting (Vercel, Netlify, AWS S3, etc.)
- Update API endpoint to production server

## License

MIT License - Feel free to use this project for learning and development.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Support

For questions or issues, please open an issue on GitHub or contact the maintainers.

```

### Get product by ID
```bash
curl http://localhost:8000/products/1
```

### Create a new product
```bash
curl -X POST "http://localhost:8000/products/" \
     -H "Content-Type: application/json" \
     -d '{
       "id": 5,
       "name": "Monitor",
       "description": "4K monitor",
       "price": 299.99,
       "quantity": 15
     }'
```

## Models

### Product
- `id`: integer
- `name`: string
- `description`: string
- `price`: float
- `quantity`: integer

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation using Python type hints
- [Uvicorn](https://www.uvicorn.org/) - ASGI server implementation