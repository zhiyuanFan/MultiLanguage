# MultiLanguage
  * 使用安卓默認的strings.xml文件 和 翻譯文檔excel，  來生成新的語言的strings.xml文件。 
  * 翻譯文檔excel只有兩列： key , Value。 key 對應strings.xml文件中的name, value對應翻譯的文本。

# Dependencies:
  * wxPython
  * xlrd
  * shutil
 
 # Use pyinstaller to create .app file
 ```
 pip3 install pyinstaller
 pyinstaller ConvertGUI.py --noconsole
 ```
