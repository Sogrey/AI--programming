# 背景去除网页工具

![应用截图](https://via.placeholder.com/800x500?text=Background+Remover+Screenshot)

基于Flask的网页应用，使用Rembg实现图像背景去除，支持实时预览和对比功能。

## ✨ 功能特性
- 🖱️ 拖放上传图片
- 🎨 自动背景去除
- 🔍 并排对比滑块
- 📱 响应式设计
- ⏳ 实时处理状态显示
- 🚫 文件类型和大小验证

## 🚀 安装指南

### 环境要求
- Python 3.7+
- pip包管理器

### 快速开始
```bash
# 克隆仓库
git clone https://github.com/yourusername/background-remover.git
cd background-remover

# 安装依赖
pip install -r requirements.txt

# 运行应用
python app.py
```
访问应用: http://localhost:5000

## 🧪 测试指南

### 功能测试
1. **基本上传测试**
   - 拖放图片(JPG/PNG)到上传区域
   - 验证背景是否成功去除
   - 检查结果图片质量
   - 测试对比滑块功能

2. **验证测试**
   - 尝试上传非图片文件(应被拒绝)
   - 尝试上传>5MB的图片(应显示错误)
   - 测试透明PNG图片

3. **性能测试**
   - 连续上传多张图片
   - 检查处理时间(通常2-5秒/张)

## 🌐 浏览器支持
| 浏览器       | 版本要求       |
|--------------|---------------|
| Chrome       | 最新版        |
| Firefox      | 最新版        |
| Edge         | 最新版        |
| Safari       | 12+           |

## 🔧 常见问题

### 常见错误
1. **依赖问题**
```bash
# 重新安装依赖
pip install --upgrade -r requirements.txt
```

2. **图片处理失败**
- 检查控制台日志
- 确认图片格式(JPG/PNG)
- 尝试较小图片(<1MB测试用)
- 检查前景/背景对比度

3. **空白结果**
- 检查浏览器控制台(F12)
- 尝试不同图片(前景明确)
- 查看服务器日志

## 🛠 开发指南

### 技术栈
- Python 3.10
- Flask 2.0
- Rembg 2.0
- ONNX Runtime 1.10
- Dropzone.js
- JuxtaposeJS

### 项目结构
```
/background-remover
├── app.py              # Flask主程序
├── requirements.txt    # 生产环境依赖
├── requirements-dev.txt # 开发环境依赖
├── static/            # 静态资源
└── templates/
    └── index.html      # 主界面
```

### 开发环境
```bash
# 安装开发依赖
pip install -r requirements-dev.txt

# 调试模式运行
python app.py
```

## 🤝 贡献指南
1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m '添加了某个特性'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 提交Pull Request

## 📜 开源协议
MIT 许可证 - 详见 [LICENSE](LICENSE) 文件