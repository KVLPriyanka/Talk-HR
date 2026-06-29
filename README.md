# HR Portal - Full Stack Web Application

A complete full-stack web application for HR Management built with Flask, MySQL, HTML5, CSS3, and JavaScript.

## 📋 Features

### For Applicants
- ✅ User Registration & Authentication
- ✅ Submit Feedback, Complaints, and Suggestions
- ✅ View Submission History with Status
- ✅ Real-time Notifications
- ✅ Responsive Mobile Design

### For HR Management
- ✅ Dashboard with Master Ticket List
- ✅ Ticket Review and Status Updates
- ✅ User Management (Activate/Deactivate)
- ✅ Advanced Filtering and Search
- ✅ HR Response Notes

## 🏗️ Project Structure

```
HR_Portal/
├── app.py                          # Main Flask application entry point
├── requirements.txt                # Python dependencies
│
├── app/
│   ├── __init__.py                # Flask app factory
│   ├── config.py                  # Configuration settings
│   ├── models.py                  # SQLAlchemy database models
│   └── routes.py                  # Flask routes and API endpoints
│
├── templates/
│   ├── index.html                 # Login/Register page
│   ├── dashboard.html             # Applicant dashboard
│   └── hr-dashboard.html          # HR management dashboard
│
└── static/
    ├── css/
    │   └── style.css              # Main stylesheet
    └── js/
        └── app.js                 # JavaScript utilities
```

## 🚀 Installation & Setup

### 1. Prerequisites
- Python 3.8+
- MySQL 5.7+ or MySQL 8.0+
- Git (optional)

### 2. Install Python Dependencies

```bash
cd "c:\Users\udayk\Downloads\HR_Portal\HR\HR"
pip install -r requirements.txt
```

### 3. Configure MySQL Connection

Edit `app/config.py` and update the database configuration:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",        # Your MySQL password
    "database": "hr_portal",
    "port": 3306
}
```

### 4. Initialize Database

The application will automatically create the database and tables when you run it for the first time.

### 5. Run the Application

```bash
python app.py
```

The application will start on: **http://localhost:5000**

## 📱 Usage

### Default Credentials

**HR Account:**
- Email: `hr@portal.com`
- Password: `hrpass123`

### For New Applicants

1. Go to Home page
2. Click "Sign Up" tab
3. Fill in your details:
   - Full Name
   - Email Address
   - Mobile Number (10 digits)
   - Employee ID
   - Password
4. Click "Create Account"
5. Login with your credentials

### Submitting Requests (Applicants)

1. Login to your account
2. Click "Submit Request"
3. Select type: Feedback, Complaint, or Suggestion
4. Enter Subject and Description
5. Click "Submit Request"
6. View status in "My Submissions"

### Managing Tickets (HR)

1. Login with HR account
2. Go to "All Tickets" tab
3. View list of all submissions
4. Click "Review" to open ticket
5. Update status and add HR response
6. Click "Update Ticket"

### Managing Users (HR)

1. Go to "Manage Users" tab
2. View all registered users
3. Toggle Active/Inactive status as needed

## 🔧 API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `POST /api/auth/register` - Create new account
- `POST /api/auth/reset-password` - Reset password
- `GET /api/auth/current` - Get current user

### Tickets (Applicant)
- `GET /api/tickets` - Get user's tickets
- `POST /api/tickets` - Create new ticket
- `GET /api/tickets/<id>` - Get ticket details

### Tickets (HR)
- `GET /api/tickets/all` - Get all tickets
- `PUT /api/tickets/<id>` - Update ticket

### Users (HR)
- `GET /api/users` - Get all users
- `POST /api/users/<username>/toggle` - Toggle user status

## 📊 Database Schema

### Users Table
```sql
- username (VARCHAR, PRIMARY KEY)
- password (VARCHAR)
- role (VARCHAR) - 'Applicant' or 'HR'
- full_name (VARCHAR)
- mobile_number (VARCHAR)
- employee_id (VARCHAR)
- is_active (BOOLEAN)
- created_at (DATETIME)
```

### Tickets Table
```sql
- id (INT, PRIMARY KEY, AUTO_INCREMENT)
- username (VARCHAR, FOREIGN KEY)
- type (VARCHAR) - 'Feedback', 'Complaint', 'Suggestion'
- subject (VARCHAR)
- description (TEXT)
- status (VARCHAR) - 'Pending Review', 'Action Taken', 'Resolved'
- hr_notes (TEXT)
- created_at (DATETIME)
- updated_at (DATETIME)
```

## 🎨 Frontend

### Technology Stack
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with CSS Grid and Flexbox
- **JavaScript (Vanilla)** - No dependencies

### Features
- Responsive design (Mobile, Tablet, Desktop)
- Dark mode support
- Real-time updates
- Form validation
- Error handling
- Loading states
- Toast notifications

## 🔐 Security Features

- ✅ Password hashing (SHA256)
- ✅ Session management
- ✅ CORS enabled
- ✅ Input validation
- ✅ SQL injection prevention (using SQLAlchemy ORM)
- ✅ CSRF protection ready

## 🐛 Troubleshooting

### MySQL Connection Error
```
Error: Cannot connect to MySQL server
Solution: Check MySQL credentials in app/config.py
```

### Port Already in Use
```
Error: Port 5000 is already in use
Solution: Change port in app.py or kill the process using port 5000
```

### Database Not Found
```
Error: Unknown database 'hr_portal'
Solution: Application creates it automatically on first run
```

### Dependencies Missing
```
Error: ModuleNotFoundError
Solution: Run: pip install -r requirements.txt
```

## 📈 Performance Optimization

- Database indexing on frequently queried columns
- Connection pooling with SQLAlchemy
- Client-side form validation
- Efficient API design
- CSS minification ready

## 🔄 Updates & Maintenance

### Adding New Fields to User
1. Update `User` model in `app/models.py`
2. SQLAlchemy will handle database migration on next run
3. Update frontend forms if needed

### Adding New Form Types
1. Add to dropdown in `templates/index.html` and `templates/dashboard.html`
2. No backend changes needed - uses generic ticket system

## 📝 License

This project is open source and available for educational and commercial use.

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify MySQL is running
3. Check Python version (3.8+)
4. Verify all dependencies installed

---

**Built with ❤️ using Flask & MySQL**

Last Updated: 2024
