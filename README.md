# TruckPro Garage Website

A professional truck garage and welding services website built with Django.

## Features

- **Responsive Design** - Mobile-friendly layout with modern CSS
- **Service Showcase** - Display truck repair, welding, and body repair services
- **Gallery** - Image gallery of completed projects
- **Contact Form** - Easy customer inquiry submission
- **About Section** - Information about the garage
- **Location & Contact Info** - Map and contact details
- **CTA Sections** - Call-to-action for quote requests

## Technologies Used

- **Backend**: Django 6.0
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite
- **Icons**: Font Awesome 6.5.1
- **Fonts**: Google Fonts (Poppins, Roboto)
- **Static Files**: WhiteNoise for production serving

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/MohammadAfzal101/truck-garage-website.git
cd truck_garage_website
```

2. **Create virtual environment**
```bash
python -m venv myenv
```

3. **Activate virtual environment**
```bash
# On Windows
myenv\Scripts\activate

# On macOS/Linux
source myenv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Run migrations**
```bash
cd garage_site
python manage.py migrate
```

6. **Start development server**
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to view the website.

## Project Structure

```
truck_garage_website/
├── garage_site/           # Django project folder
│   ├── settings.py        # Project settings
│   ├── urls.py            # Project URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── main/                  # Main Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
├── templates/main/        # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── services.html
│   ├── gallery.html
│   ├── about.html
│   ├── contact.html
│   └── ...
├── static/                # Static files
│   ├── css/               # Stylesheets
│   │   ├── base.css
│   │   ├── hero.css
│   │   ├── services.css
│   │   ├── gallery.css
│   │   └── ...
│   └── images/            # Images and logos
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Configuration

### Debug Mode
- **Development**: `DEBUG = True` (in `garage_site/settings.py`)
- **Production**: `DEBUG = False` (requires static file serving setup)

### Database
Default SQLite database: `db.sqlite3`

To use PostgreSQL or MySQL, update `DATABASES` in `settings.py`.

## Usage

### Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

Then visit `http://localhost:8000/admin` to manage content.

### Collect Static Files (Production)
```bash
python manage.py collectstatic
```

## Pages

- **Home** (`/`) - Landing page with hero section
- **Services** (`/services/`) - Service offerings
- **Gallery** (`/gallery/`) - Project gallery
- **About** (`/about/`) - About the garage
- **Contact** (`/contact/`) - Contact form

## Customization

### Change Colors
Update CSS variables in the CSS files under `static/css/`:
- Primary color: `#f5b400` (yellow/gold)
- Background: `#1c1c1c` (dark)
- Text: `#ffffff` (white)

### Add Services
Edit the services section in `templates/main/services.html`

### Update Contact Info
Modify footer contact details in `templates/main/base.html`

## Deployment

### Using Gunicorn
```bash
pip install gunicorn
gunicorn garage_site.wsgi:application --bind 0.0.0.0:8000
```

### Using Heroku
1. Create `Procfile`:
```
web: gunicorn garage_site.wsgi
```

2. Deploy:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

## Security Notes

⚠️ **Important for Production:**
- Change `SECRET_KEY` in `settings.py`
- Set `DEBUG = False`
- Use `HTTPS`
- Update `ALLOWED_HOSTS`
- Use environment variables for sensitive data

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the MIT License.

## Contact

**TruckPro Garage**
- Email: superfix.truckgarage@gmail.com
- Phone: 7039475132
- Location: Wadi Bunder Traffic Police Station

## Author

[Mohammed Afzal](https://github.com/MohammadAfzal101)

---

**Last Updated**: March 2026
