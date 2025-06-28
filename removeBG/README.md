# Background Remover Web Tool

![App Screenshot](https://via.placeholder.com/800x500?text=Background+Remover+Screenshot)

A Flask-based web application for removing image backgrounds using Rembg with real-time preview and comparison.

## ✨ Features
- 🖱️ Drag & drop image upload
- 🎨 Automatic background removal
- 🔍 Side-by-side comparison slider
- 📱 Responsive design
- ⏳ Real-time processing status
- 🚫 File type and size validation

## 🚀 Installation

### Prerequisites
- Python 3.7+
- pip

### Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/background-remover.git
cd background-remover

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```
Access the application at: http://localhost:5000

## 🧪 Testing

### Functional Tests
1. **Basic Upload Test**
   - Drag an image (JPG/PNG) onto the upload area
   - Verify the background is removed
   - Check the result image quality
   - Test the comparison slider

2. **Validation Tests**
   - Try uploading non-image files (should be rejected)
   - Try uploading images >5MB (should show error)
   - Test with transparent PNGs

3. **Performance**
   - Upload multiple images sequentially
   - Check processing time (typically 2-5 seconds per image)

## 🌐 Browser Support
| Browser       | Version       |
|---------------|---------------|
| Chrome        | Latest        |
| Firefox       | Latest        |
| Edge          | Latest        |
| Safari        | 12+           |

## 🔧 Troubleshooting

### Common Issues
1. **Dependency Errors**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

2. **Image Processing Failures**
- Check console logs
- Verify image format (JPG/PNG)
- Try smaller image (<1MB for testing)
- Check foreground/background contrast

3. **Blank Results**
- Check browser console (F12)
- Try different image with clear foreground
- Verify server logs

## 🛠 Development

### Tech Stack
- Python 3.10
- Flask 2.0
- Rembg 2.0
- ONNX Runtime 1.10
- Dropzone.js
- JuxtaposeJS

### Project Structure
```
/background-remover
├── app.py              # Flask application
├── requirements.txt    # Production dependencies
├── requirements-dev.txt # Development dependencies
├── static/            # Static assets
└── templates/
    └── index.html      # Main interface
```

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run in debug mode
python app.py
```

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License
MIT License - see [LICENSE](LICENSE) for details