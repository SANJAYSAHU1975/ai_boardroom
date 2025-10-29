# AI Boardroom

An intelligent board management system designed to enhance governance, streamline meetings, and improve decision-making processes for boards of directors.

## 🎯 Features

### Meeting Management
- Schedule and organize board meetings
- Create detailed meeting agendas
- Track meeting status (scheduled, in-progress, completed, cancelled)
- Record and maintain comprehensive meeting minutes

### Document Repository
- Centralized document storage
- Support for multiple document types (financial reports, strategic plans, policies, etc.)
- Document categorization and metadata
- Quick access to board materials

### AI-Powered Capabilities
- Automated meeting summarization
- Action item extraction
- Key points identification
- Content analysis and insights

### Governance Tools
- Agenda item management with time allocation
- Meeting minutes with action item tracking
- Decision documentation
- Historical meeting records

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/SANJAYSAHU1975/ai_boardroom.git
cd ai_boardroom
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run the application:
```bash
python app.py
```

6. Open your browser and navigate to:
```
http://localhost:5000
```

## 📁 Project Structure

```
ai_boardroom/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
├── templates/             # HTML templates
│   └── index.html         # Main web interface
└── README.md              # This file
```

## 🔧 Configuration

The application can be configured using environment variables in the `.env` file:

- `FLASK_APP`: Application entry point (default: app.py)
- `FLASK_ENV`: Development or production mode
- `SECRET_KEY`: Secret key for session management (⚠️ **REQUIRED** - must be set to a strong random value)
- `DATABASE_URL`: Database connection string (default: sqlite:///boardroom.db)
- `OPENAI_API_KEY`: OpenAI API key for AI features (optional)

### Security Note
⚠️ **Important**: Always set a strong, random `SECRET_KEY` in production. Never use the default values from `.env.example`. You can generate a secure key using:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

## 📡 API Endpoints

### Meetings
- `GET /api/meetings` - List all meetings
- `POST /api/meetings` - Create a new meeting
- `GET /api/meetings/<id>` - Get meeting details
- `PUT /api/meetings/<id>` - Update a meeting
- `DELETE /api/meetings/<id>` - Delete a meeting

### Agenda Items
- `GET /api/meetings/<id>/agenda` - List agenda items for a meeting
- `POST /api/meetings/<id>/agenda` - Add agenda item
- `PUT /api/agenda/<id>` - Update agenda item
- `DELETE /api/agenda/<id>` - Delete agenda item

### Documents
- `GET /api/documents` - List all documents
- `POST /api/documents` - Upload a new document
- `GET /api/documents/<id>` - Get document details
- `PUT /api/documents/<id>` - Update a document
- `DELETE /api/documents/<id>` - Delete a document

### Meeting Minutes
- `GET /api/meetings/<id>/minutes` - List minutes for a meeting
- `POST /api/meetings/<id>/minutes` - Add meeting minutes
- `PUT /api/minutes/<id>` - Update minutes
- `DELETE /api/minutes/<id>` - Delete minutes

### AI Features
- `POST /api/summarize` - Generate AI summary of content

## 💻 Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLAlchemy with SQLite
- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **AI**: OpenAI API integration (optional)

## 🎨 User Interface

The application features a modern, responsive web interface with:
- Dashboard with feature overview
- Meeting management interface
- Document repository
- Modal dialogs for creating/editing content
- Responsive design for desktop and mobile

## 🔒 Security

- Environment-based configuration
- SQL injection protection through SQLAlchemy ORM
- CORS support for API access
- Session management with secret keys

## 📝 Usage Examples

### Creating a Meeting

```python
import requests

meeting_data = {
    "title": "Q1 Board Meeting",
    "description": "Quarterly board review and strategic planning",
    "date": "2025-01-15T10:00:00",
    "status": "scheduled"
}

response = requests.post(
    "http://localhost:5000/api/meetings",
    json=meeting_data
)
```

### Adding Meeting Minutes

```python
minutes_data = {
    "content": "Full meeting transcript...",
    "summary": "Key decisions and discussions...",
    "action_items": "1. Review budget proposal\n2. Schedule follow-up"
}

response = requests.post(
    f"http://localhost:5000/api/meetings/{meeting_id}/minutes",
    json=minutes_data
)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🌟 Key Benefits

- **Efficiency**: Streamline board operations and reduce administrative overhead
- **Transparency**: Improve information sharing and governance visibility
- **Intelligence**: Leverage AI for insights and automated summarization
- **Organization**: Keep all board materials and decisions in one place
- **Collaboration**: Enable better communication between board members

## 🚧 Future Enhancements

- User authentication and role-based access control
- Email notifications for meetings and action items
- File upload support for documents
- Advanced AI summarization with OpenAI GPT
- Calendar integration
- Mobile app
- Reporting and analytics dashboard
- Voting and decision tracking
- Audit trail and compliance features

## 📞 Support

For questions, issues, or suggestions, please open an issue on GitHub.