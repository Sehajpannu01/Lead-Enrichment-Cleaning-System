# Lead Enrichment & Cleaning System

A comprehensive data pipeline system for extracting, transforming, and loading lead data from external APIs. This system is designed to enrich and clean lead data for business intelligence and analytics purposes.

## Features

- **Data Extraction**: Automated data extraction from RandomUser API
- **Data Transformation**: Flattening nested JSON structures and data cleaning
- **Data Loading**: Structured data loading capabilities
- **Error Handling**: Robust retry mechanisms and error handling
- **Environment Configuration**: Secure configuration management with environment variables
- **Docker Support**: Containerized deployment ready
- **Airflow Integration**: DAG-based workflow orchestration

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)
- Docker (optional, for containerized deployment)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Lead Enrichment & Cleaning System"
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   API_KEY=your_api_key_here
   POSTGRES_USER=your_db_user
   POSTGRES_PASS=your_db_password
   DB_NAME=your_database_name
   ```

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_KEY` | RandomUser API key | Yes |
| `POSTGRES_USER` | PostgreSQL username | Yes |
| `POSTGRES_PASS` | PostgreSQL password | Yes |
| `DB_NAME` | Database name | Yes |

### API Configuration

The system uses the RandomUser API to generate sample user data. You can customize the extraction by modifying parameters in `Scripts/extract.py`:

- `num_results`: Number of records to extract (default: 500)
- `results_per_call`: Records per API call (default: 100)
- Nationality filter: Add `&nat=us,gb,ca` to API URL for specific countries

## Usage

### Basic Usage

Run the complete pipeline:
```bash
python main.py
```

### Individual Components

**Extract data only:**
```bash
python Scripts/extract.py
```

**Transform data:**
```bash
python Scripts/transform.py
```

**Load data:**
```bash
python Scripts/load.py
```

### Data Pipeline Flow

1. **Extract**: Fetches user data from RandomUser API
2. **Transform**: Flattens nested JSON and cleans data
3. **Load**: Stores processed data in the database

## Project Structure

```
Lead Enrichment & Cleaning System/
├── Dags/                    # Airflow DAG files
├── Data/                    # Data storage directory
├── Docker/                  # Docker configuration files
├── Scripts/                 # Core pipeline scripts
│   ├── extract.py          # Data extraction module
│   ├── transform.py        # Data transformation module
│   └── load.py             # Data loading module
├── main.py                 # Main pipeline orchestrator
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## API Details

### RandomUser API

- **Endpoint**: `https://randomuser.me/api/`
- **Rate Limiting**: Handled with retry logic
- **Parameters**:
  - `results`: Number of users to fetch
  - `nat`: Nationality filter (us, gb, ca, au, etc.)
- **Response Format**: Nested JSON with user details

### Data Schema

The extracted data includes:
- Personal information (name, gender, email)
- Location details (address, city, country)
- Contact information (phone, cell)
- Authentication data (login credentials)
- Demographics (date of birth, nationality)
- Profile pictures and metadata

## Docker Support

The project includes Docker support for containerized deployment:

```bash
# Build the Docker image
docker build -t lead-enrichment-system .

# Run the container
docker run --env-file .env lead-enrichment-system
```

## Troubleshooting

### Common Issues

1. **API Key Not Found**
   - Ensure `.env` file is in the project root
   - Check that `API_KEY` variable is set correctly

2. **Data Type Errors**
   - Verify data transformation is working correctly
   - Check that pandas DataFrame is created properly

3. **Import Errors**
   - Ensure all dependencies are installed
   - Check Python path and virtual environment

### Debug Mode

Enable debug logging by adding print statements or using Python's logging module:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Development Notes

- The system uses pandas for data manipulation
- JSON normalization handles nested API responses
- Retry logic ensures robust API calls
- Environment variables provide secure configuration

## Testing

Run tests to ensure everything works correctly:
```bash
python -m pytest tests/
```

## Data Output

The system generates cleaned, structured data suitable for:
- Business intelligence dashboards
- Lead scoring models
- Customer analytics
- Marketing campaigns

## Security

- API keys and credentials are stored in environment variables
- Database connections use secure authentication
- No sensitive data is hardcoded in the source code

## Performance

- Batch processing for efficient API usage
- Configurable batch sizes for memory optimization
- Retry mechanisms prevent data loss

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the project documentation
3. Create an issue in the repository

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Made with love for efficient lead data processing** 