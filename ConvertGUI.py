# -*- coding: utf-8 -*-

import wx
import ConvertUtil as util

excel_src_path = []
xml_src_path = []


def excelBtnOnClick(event):
    # Create open file dialog
    openFileDialog = wx.FileDialog(frame, "Open", "", "",
                                   "Excel files (*.xlsx)|*.xlsx",
                                   wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
    openFileDialog.ShowModal()
    excelPathLabel.LabelText = openFileDialog.GetPath()
    excel_src_path.append(openFileDialog.GetPath())
    openFileDialog.Destroy()


def xmlBtnOnClick(event):
    # Create open file dialog
    openFileDialog = wx.FileDialog(frame, "Open", "", "",
                                   "Xml files (*.xml)|*.xml",
                                   wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
    openFileDialog.ShowModal()
    xmlPathLabel.LabelText = openFileDialog.GetPath()
    xml_src_path.append(openFileDialog.GetPath())
    openFileDialog.Destroy()

def genBtnOnClick(event):
    if len(excel_src_path) == 0:
        return
    if len(xml_src_path) == 0:
        return
    desPath = util.deal_with_excel_and_xml(excel_src_path[0], xml_src_path[0])
    newXmlPathLabel.LabelText = desPath


app = wx.App()
frame = wx.Frame(None, -1, 'Generate Multi-Language Tool')
frame.SetDimensions(0,0,600,300)

panel = wx.Panel(frame, wx.ID_ANY)

excelBtn = wx.Button(panel, wx.ID_ANY, 'choose xlsx file...', (10, 10))
excelBtn.Bind(wx.EVT_BUTTON, excelBtnOnClick)
excelPathLabel = wx.StaticText(panel, wx.ID_ANY, pos=(10, 40), style=wx.ALIGN_LEFT)

xmlBtn = wx.Button(panel, wx.ID_ANY, 'choose xml file...', (10, 80))
xmlBtn.Bind(wx.EVT_BUTTON, xmlBtnOnClick)
xmlPathLabel = wx.StaticText(panel, wx.ID_ANY, pos=(10, 110), style=wx.ALIGN_LEFT)

genBtn = wx.Button(panel, wx.ID_ANY, 'genenrate new xml file...', (10, 150))
genBtn.Bind(wx.EVT_BUTTON, genBtnOnClick)
newXmlPathLabel = wx.StaticText(panel, wx.ID_ANY, pos=(10, 180), style=wx.ALIGN_LEFT)

frame.Show()
frame.Centre()
app.MainLoop()
