"""
QR Code Generator for HR Portal Mobile Testing (Public Over Internet)
"""
import qrcode
import os
from pathlib import Path

# 🌟 YOUR ACTIVE LIVE NGROK PUBLIC GATEWAY URL
NETWORK_URL = "https://limit-game-density.ngrok-free.dev"

def create_portal_qr():
    print(f"Generating Public QR Code pointing to: {NETWORK_URL}")
    
    # Configure the QR code properties
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    
    qr.add_data(NETWORK_URL)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # 1. Save to Root Project Folder
    root_filename = "hr_portal_qr.png"
    img.save(root_filename)
    print(f"✓ Success! QR code saved to Root: '{os.path.abspath(root_filename)}'")
    
    # 2. Save to Output Directory (For Streamlit/App alignment)
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    output_filepath = output_dir / "portal_qr.png"
    img.save(output_filepath)
    print(f"✓ Success! QR code saved to Output folder: '{output_filepath.resolve()}'")
    
    print("\n👉 Scan either image with ANY mobile phone anywhere in the world to access your portal!")

if __name__ == "__main__":
    create_portal_qr()



# """
# QR Code Generator for HR Portal Mobile Testing (Local Wi-Fi Network)
# """
# import qrcode
# import os
# from pathlib import Path

# # 🌟 YOUR COMPUTER'S LOCAL WI-FI IP ADDRESS
# # Make sure your phone is connected to the exact same Wi-Fi network!
# NETWORK_URL = "http://192.168.15.175:5000"

# def create_portal_qr():
#     print(f"Generating Local Network QR Code pointing to: {NETWORK_URL}")
    
#     # Configure the QR code properties
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_M,
#         box_size=10,
#         border=4,
#     )
    
#     qr.add_data(NETWORK_URL)
#     qr.make(fit=True)

#     img = qr.make_image(fill_color="black", back_color="white")
    
#     # 1. Save to Root Project Folder
#     root_filename = "hr_portal_qr.png"
#     img.save(root_filename)
#     print(f"✓ Success! QR code saved to Root: '{os.path.abspath(root_filename)}'")
    
#     # 2. Save to Output Directory
#     output_dir = Path("output")
#     output_dir.mkdir(exist_ok=True)
#     output_filepath = output_dir / "portal_qr.png"
#     img.save(output_filepath)
#     print(f"✓ Success! QR code saved to Output folder: '{output_filepath.resolve()}'")
    
#     print("\n👉 Ensure your phone is on the SAME Wi-Fi, then scan the image!")

# if __name__ == "__main__":
#     create_portal_qr()



# """
# Network-Independent Automated QR Code Generator
# """
# import qrcode
# import os
# import requests
# from pathlib import Path

# def get_live_ngrok_url():
#     """Automatically fetches the active public URL from the local ngrok agent API"""
#     try:
#         # Ngrok exposes a local status API on port 4040 while running
#         response = requests.get("http://127.0.0.1:4040/api/tunnels", timeout=2)
#         tunnels = response.json().get('tunnels', [])
#         for tunnel in tunnels:
#             if tunnel.get('proto') == 'https':
#                 return tunnel.get('public_url')
#     except Exception:
#         pass
#     return None

# def create_portal_qr():
#     # 🔄 Auto-detect public link, fallback to local network if ngrok is off
#     public_url = get_live_ngrok_url()
    
#     if public_url:
#         NETWORK_URL = public_url
#         print(f"🌐 [GLOBAL MODE] Found active ngrok tunnel: {NETWORK_URL}")
#     else:
#         NETWORK_URL = "http://192.168.15.175:5000"
#         print(f"🏠 [LOCAL MODE] ngrok isn't running. Falling back to local Wi-Fi: {NETWORK_URL}")
    
#     # Configure QR configuration
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_M,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(NETWORK_URL)
#     qr.make(fit=True)
#     img = qr.make_image(fill_color="black", back_color="white")
    
#     # Save destinations
#     root_filename = "hr_portal_qr.png"
#     img.save(root_filename)
    
#     output_dir = Path("output")
#     output_dir.mkdir(exist_ok=True)
#     img.save(output_dir / "portal_qr.png")
    
#     print(f"✓ Success! Updated QR code saved.")
#     print("👉 Scan the image to open the portal seamlessly.")

# if __name__ == "__main__":
#     # Ensure requests library is available
#     try:
#         import requests
#     except ImportError:
#         os.system('pip install requests')
#         import requests
        
#     create_portal_qr()


# """
# Network-Independent QR Code Generator (Using LocalTunnel - No Ngrok)
# """
# import qrcode
# import os
# import subprocess
# import time
# import re
# from pathlib import Path

# def start_localtunnel():
#     """Starts localtunnel on port 5000 and grabs the public URL automatically"""
#     print("🌐 Spinning up a secure public tunnel via LocalTunnel...")
    
#     # Run localtunnel using npx (built into Node.js/Windows if installed)
#     # If Node isn't installed, it fallbacks gracefully
#     try:
#         process = subprocess.Popen(
#             "npx localtunnel --port 5000", 
#             stdout=subprocess.PIPE, 
#             stderr=subprocess.PIPE, 
#             text=True, 
#             shell=True
#         )
        
#         # Give it a couple of seconds to establish the connection
#         time.sleep(3)
        
#         # Read the console output to find the public URL
#         for _ in range(5):
#             output = process.stdout.readline()
#             if "url is" in output.lower():
#                 url = re.search(r'https://[^\s]+', output)
#                 if url:
#                     return url.group(0)
#             time.sleep(1)
#     except Exception as e:
#         print(f"❌ Could not start LocalTunnel automatically: {e}")
#     return None

# def create_portal_qr():
#     public_url = start_localtunnel()
    
#     if public_url:
#         NETWORK_URL = public_url
#         print(f"✅ [GLOBAL PUBLIC LINK]: {NETWORK_URL}")
#     else:
#         # Absolute fallback to local Wi-Fi if no internet tunnel can be made
#         NETWORK_URL = "http://192.168.15.175:5000"
#         print(f"⚠️ LocalTunnel failed. Falling back to local network IP: {NETWORK_URL}")
    
#     # Generate the QR Code graphic
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_M,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(NETWORK_URL)
#     qr.make(fit=True)
#     img = qr.make_image(fill_color="black", back_color="white")
    
#     # Save the files
#     root_filename = "hr_portal_qr.png"
#     img.save(root_filename)
    
#     output_dir = Path("output")
#     output_dir.mkdir(exist_ok=True)
#     img.save(output_dir / "portal_qr.png")
    
#     print(f"\n✓ Success! QR code updated.")
#     print("👉 Keep this terminal window open so the link stays active!")
#     print("👉 Scan the image with any phone (Wi-Fi or Mobile Data) to test.")

# if __name__ == "__main__":
#     create_portal_qr()
#     # Keep the script running to sustain the tunnel connection
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("\nStopping public tunnel. Goodbye!")



# """
# QR Code Generator for HR Portal Mobile Testing (Public Over Internet - No Ngrok)
# """
# import qrcode
# import os
# from pathlib import Path

# # 🌟 PASTE YOUR LIVE PINGGY URL HERE
# NETWORK_URL = "http://127.0.0.1:5000/"

# def create_portal_qr():
#     print(f"Generating Public QR Code pointing to: {NETWORK_URL}")
    
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_M,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(NETWORK_URL)
#     qr.make(fit=True)
#     img = qr.make_image(fill_color="black", back_color="white")
    
#     root_filename = "hr_portal_qr.png"
#     img.save(root_filename)
    
#     output_dir = Path("output")
#     output_dir.mkdir(exist_ok=True)
#     img.save(output_dir / "portal_qr.png")
    
#     print(f"✓ Success! New non-ngrok QR code saved.")

# if __name__ == "__main__":
#     create_portal_qr()