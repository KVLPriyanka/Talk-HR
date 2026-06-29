"""
HR Portal - Full Stack Web Application
Main Entry Point
"""

import os
from app import create_app

app = create_app(os.environ.get("FLASK_ENV", "development"))

if __name__ == "__main__":
    print("=" * 70)
    print("  HR Portal - Full Stack Web Application")
    print("=" * 70)
    print("\n✓ Database: MySQL")
    print("✓ Backend: Flask")
    print("✓ Frontend: HTML/CSS/JavaScript")
    print("\n🚀 Starting server...")
    print("📱 Open browser: http://localhost:5000")
    print("\n" + "=" * 70 + "\n")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=True
    )