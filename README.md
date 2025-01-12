# 在安卓手机上使用ncnn部署自己的yolo11模型
1. 使用 https://github.com/PIPIKAI/ultralytics/tree/triplemu/model-only 仓库代码导出ncnn
2. 使用 https://github.com/PIPIKAI/android-ncnn-yolo11 构建安卓apk
3. 修改 java/com/pipikai/android_ncnn_yolo11/MainActivity.kt 文件中showObjects函数 textpaint.textSize 修改字体大小 paint.strokeWidth修改矩形框大小
4. 修改res/values/strings.xml 文件 修改"labels" ，model
