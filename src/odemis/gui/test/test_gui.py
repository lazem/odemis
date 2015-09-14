# This file was automatically generated by pywxrc.
# -*- coding: UTF-8 -*-

import wx
import wx.xrc as xrc

__res = None

def get_resources():
    """ This function provides access to the XML resources in this module."""
    global __res
    if __res == None:
        __init_resources()
    return __res




class xrctext_frame(wx.Frame):
#!XRCED:begin-block:xrctext_frame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrctext_frame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "text_frame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.text_panel = xrc.XRCCTRL(self, "text_panel")
        self.txt_suggest = xrc.XRCCTRL(self, "txt_suggest")
        self.unit_float_label = xrc.XRCCTRL(self, "unit_float_label")
        self.unit_float = xrc.XRCCTRL(self, "unit_float")
        self.txt_odcbox = xrc.XRCCTRL(self, "txt_odcbox")



class xrcstream_frame(wx.Frame):
#!XRCED:begin-block:xrcstream_frame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcstream_frame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "stream_frame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.scrwin = xrc.XRCCTRL(self, "scrwin")
        self.fpb = xrc.XRCCTRL(self, "fpb")
        self.stream_bar = xrc.XRCCTRL(self, "stream_bar")



class xrcbutton_frame(wx.Frame):
#!XRCED:begin-block:xrcbutton_frame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcbutton_frame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "button_frame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.button_panel = xrc.XRCCTRL(self, "button_panel")



class xrccanvas_frame(wx.Frame):
#!XRCED:begin-block:xrccanvas_frame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrccanvas_frame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "canvas_frame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.canvas_panel = xrc.XRCCTRL(self, "canvas_panel")



class xrcfpb_frame(wx.Frame):
#!XRCED:begin-block:xrcfpb_frame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcfpb_frame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "fpb_frame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.scrwin = xrc.XRCCTRL(self, "scrwin")
        self.fpb = xrc.XRCCTRL(self, "fpb")
        self.panel_1 = xrc.XRCCTRL(self, "panel_1")
        self.panel_2 = xrc.XRCCTRL(self, "panel_2")
        self.panel_3 = xrc.XRCCTRL(self, "panel_3")



class xrcgrid_frame(wx.Frame):
#!XRCED:begin-block:xrcgrid_frame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcgrid_frame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "grid_frame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.grid_panel = xrc.XRCCTRL(self, "grid_panel")
        self.red = xrc.XRCCTRL(self, "red")
        self.blue = xrc.XRCCTRL(self, "blue")
        self.purple = xrc.XRCCTRL(self, "purple")
        self.brown = xrc.XRCCTRL(self, "brown")
        self.yellow = xrc.XRCCTRL(self, "yellow")
        self.green = xrc.XRCCTRL(self, "green")



class xrcmenu_bar(wx.MenuBar):
    def __init__(self):
        pre = get_resources().LoadMenuBar("menu_bar")
        self.PostCreate(pre)
        
        # Define variables for the menu items





# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    wx.FileSystem.AddHandler(wx.MemoryFSHandler())

    test_gui_xrc = '''\
<?xml version="1.0" ?><resource version="2.5.3.0" xmlns="http://www.wxwidgets.org/wxxrc">
  <object class="wxFrame" name="text_frame">
    <object_ref ref="menu_bar"/>
    <object class="wxPanel" name="text_panel">
      <object class="wxBoxSizer">
        <orient>wxVERTICAL</orient>
        <object class="sizeritem">
          <object class="wxFlexGridSizer">
            <object class="sizeritem">
              <object class="wxStaticText">
                <label>SuggestTextCtrl</label>
              </object>
            </object>
            <object class="sizeritem">
              <object class="SuggestTextCtrl" name="txt_suggest">
                <size>200,-1</size>
                <value>suggest text field</value>
                <fg>#1E90FF</fg>
                <bg>#4D4D4D</bg>
                <style>wxBORDER_NONE</style>
                <XRCED>
                  <assign_var>1</assign_var>
                </XRCED>
              </object>
            </object>
            <object class="sizeritem">
              <object class="wxStaticText">
                <label>UnitIntegerCtrl</label>
              </object>
            </object>
            <object class="sizeritem">
              <object class="UnitIntegerCtrl">
                <size>200,-1</size>
                <value>0</value>
                <min>-10</min>
                <max>10</max>
                <unit>μm</unit>
                <fg>#1E90FF</fg>
                <bg>#4D4D4D</bg>
                <style>wxBORDER_NONE</style>
              </object>
            </object>
            <object class="sizeritem">
              <object class="wxStaticText" name="unit_float_label">
                <label>UnitFloatCtrl</label>
                <XRCED>
                  <assign_var>1</assign_var>
                </XRCED>
              </object>
            </object>
            <object class="sizeritem">
              <object class="UnitFloatCtrl" name="unit_float">
                <size>200,-1</size>
                <unit>g</unit>
                <fg>#1E90FF</fg>
                <bg>#4D4D4D</bg>
                <style>wxBORDER_NONE</style>
                <XRCED>
                  <assign_var>1</assign_var>
                </XRCED>
              </object>
            </object>
            <object class="sizeritem">
              <object class="wxStaticText">
                <label>OwnerDrawnComboBox</label>
              </object>
            </object>
            <object class="sizeritem">
              <object class="wxOwnerDrawnComboBox" name="txt_odcbox">
                <size>200,14</size>
                <content>
                  <item>aap</item>
                  <item>noot</item>
                  <item>mies</item>
                </content>
                <selection>1</selection>
                <fg>#1E90FF</fg>
                <bg>#4D4D4D</bg>
                <style>wxBORDER_NONE|wxCB_READONLY</style>
                <XRCED>
                  <assign_var>1</assign_var>
                </XRCED>
              </object>
            </object>
            <cols>2</cols>
            <vgap>5</vgap>
            <hgap>5</hgap>
          </object>
          <flag>wxALL</flag>
          <border>5</border>
        </object>
      </object>
      <fg>#E6E6FA</fg>
      <bg>#4D4D4D</bg>
      <XRCED>
        <assign_var>1</assign_var>
      </XRCED>
    </object>
    <size>400,400</size>
  </object>
  <object class="wxFrame" name="stream_frame">
    <object_ref ref="menu_bar"/>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <object class="wxScrolledWindow" name="scrwin">
          <object class="wxBoxSizer">
            <orient>wxVERTICAL</orient>
            <object class="sizeritem">
              <object class="FoldPanelBar" name="fpb">
                <object class="FoldPanelItem">
                  <object class="StreamBar" name="stream_bar">
                    <add_button>1</add_button>
                    <fg>#7F7F7F</fg>
                    <bg>#333333</bg>
                    <XRCED>
                      <assign_var>1</assign_var>
                    </XRCED>
                  </object>
                  <label>STREAMS</label>
                  <fg>#1A1A1A</fg>
                  <bg>#555555</bg>
                  <XRCED>
                    <assign_var>1</assign_var>
                  </XRCED>
                </object>
                <spacing>0</spacing>
                <leftspacing>0</leftspacing>
                <rightspacing>0</rightspacing>
                <bg>#4D4D4D</bg>
                <XRCED>
                  <assign_var>1</assign_var>
                </XRCED>
              </object>
              <flag>wxEXPAND</flag>
            </object>
          </object>
          <bg>#A52A2A</bg>
          <XRCED>
            <assign_var>1</assign_var>
          </XRCED>
        </object>
        <option>1</option>
        <flag>wxEXPAND</flag>
        <minsize>400,400</minsize>
      </object>
    </object>
    <size>400,400</size>
    <title>Stream panel test frame</title>
  </object>
  <object class="wxFrame" name="button_frame">
    <object_ref ref="menu_bar"/>
    <object class="wxPanel" name="button_panel">
      <object class="wxBoxSizer">
        <orient>wxVERTICAL</orient>
        <object class="sizeritem">
          <object class="NImageButton">
            <icon>___img_icon_ico_cam_png</icon>
            <height>48</height>
          </object>
          <flag>wxEXPAND</flag>
        </object>
      </object>
      <fg>#E6E6FA</fg>
      <bg>#4D4D4D</bg>
      <XRCED>
        <assign_var>1</assign_var>
      </XRCED>
    </object>
    <size>400,400</size>
  </object>
  <object class="wxFrame" name="canvas_frame">
    <object_ref ref="menu_bar"/>
    <object class="wxPanel" name="canvas_panel">
      <object class="wxBoxSizer">
        <orient>wxVERTICAL</orient>
      </object>
      <bg>#4D4D4D</bg>
      <XRCED>
        <assign_var>1</assign_var>
      </XRCED>
    </object>
    <size>400,400</size>
    <title>Cairo Test</title>
    <bg>#4D4D4D</bg>
  </object>
  <object class="wxFrame" name="fpb_frame">
    <object_ref ref="menu_bar"/>
    <object class="wxBoxSizer">
      <object class="sizeritem">
        <object class="wxScrolledWindow" name="scrwin">
          <object class="wxBoxSizer">
            <object class="sizeritem">
              <object class="FoldPanelBar" name="fpb">
                <object class="FoldPanelItem" name="panel_1">
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <label>Test Panel 1</label>
                  <fg>#1A1A1A</fg>
                  <bg>#666666</bg>
                  <font>
                    <size>13</size>
                    <style>normal</style>
                    <weight>normal</weight>
                    <underlined>0</underlined>
                    <face>Ubuntu</face>
                    <encoding>UTF-8</encoding>
                  </font>
                  <XRCED>
                    <assign_var>1</assign_var>
                  </XRCED>
                </object>
                <object class="FoldPanelItem" name="panel_2">
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <label>Test Panel 2</label>
                  <collapsed>1</collapsed>
                  <fg>#1A1A1A</fg>
                  <bg>#666666</bg>
                  <font>
                    <size>13</size>
                    <style>normal</style>
                    <weight>normal</weight>
                    <underlined>0</underlined>
                    <face>Ubuntu</face>
                    <encoding>UTF-8</encoding>
                  </font>
                  <XRCED>
                    <assign_var>1</assign_var>
                  </XRCED>
                </object>
                <object class="FoldPanelItem" name="panel_3">
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <object class="wxStaticText">
                    <label>LABEL</label>
                  </object>
                  <label>Test Panel 3</label>
                  <fg>#1A1A1A</fg>
                  <bg>#666666</bg>
                  <font>
                    <size>13</size>
                    <style>normal</style>
                    <weight>normal</weight>
                    <underlined>0</underlined>
                    <face>Ubuntu</face>
                    <encoding>UTF-8</encoding>
                  </font>
                  <XRCED>
                    <assign_var>1</assign_var>
                  </XRCED>
                </object>
                <spacing>0</spacing>
                <bg>#1E90FF</bg>
                <XRCED>
                  <assign_var>1</assign_var>
                </XRCED>
              </object>
              <flag>wxEXPAND</flag>
            </object>
            <orient>wxVERTICAL</orient>
          </object>
          <bg>#A52A2A</bg>
          <XRCED>
            <assign_var>1</assign_var>
          </XRCED>
        </object>
        <option>1</option>
        <flag>wxEXPAND</flag>
        <minsize>100,100</minsize>
      </object>
      <orient>wxVERTICAL</orient>
    </object>
    <title>Fold Panel Bar Test Frame</title>
    <bg>#666666</bg>
  </object>
  <object class="wxFrame" name="grid_frame">
    <object_ref ref="menu_bar"/>
    <object class="ViewportGrid" name="grid_panel">
      <object class="wxPanel" name="red">
        <bg>#E65F5F</bg>
        <XRCED>
          <assign_var>1</assign_var>
        </XRCED>
      </object>
      <object class="wxPanel" name="blue">
        <bg>#57B4BA</bg>
        <XRCED>
          <assign_var>1</assign_var>
        </XRCED>
      </object>
      <object class="wxPanel" name="purple">
        <bg>#E48BD3</bg>
        <XRCED>
          <assign_var>1</assign_var>
        </XRCED>
      </object>
      <object class="wxPanel" name="brown">
        <bg>#FFC292</bg>
        <XRCED>
          <assign_var>1</assign_var>
        </XRCED>
      </object>
      <object class="wxPanel" name="yellow">
        <bg>#FFF490</bg>
        <hidden>1</hidden>
        <XRCED>
          <assign_var>1</assign_var>
        </XRCED>
      </object>
      <object class="wxPanel" name="green">
        <bg>#B2E926</bg>
        <hidden>1</hidden>
        <XRCED>
          <assign_var>1</assign_var>
        </XRCED>
      </object>
      <size>500,500</size>
      <bg>#FFC9C9</bg>
      <XRCED>
        <assign_var>1</assign_var>
      </XRCED>
    </object>
    <size>500,500</size>
    <title>Cairo Test</title>
    <centered>1</centered>
    <bg>#1E90FF</bg>
  </object>
  <object class="wxMenuBar" name="menu_bar">
    <object class="wxMenu">
      <object class="wxMenuItem" name="item_inspect">
        <label>Inspect</label>
        <accel>Ctrl+V</accel>
      </object>
      <object class="separator"/>
      <object class="wxMenuItem">
        <label>Quit</label>
        <accel>Ctrl+Q</accel>
      </object>
      <label>Extra</label>
    </object>
  </object>
</resource>'''

    ___img_icon_ico_cam_png = '''\
\x89PNG\x0d
\x1a
\x00\x00\x00\x0dIHDR\x00\x00\x00)\x00\x00\x00\x1d\x08\x06\x00\x00\x007\
\x8bEM\x00\x00\x01\xa2IDATX\xc3\xed\x96Kj\x02A\x14Eu"\xf4Hp\x94\x0d\xb8\
\x04m\xb4\xd1VQ\xc4\x1f\xb6\x9a\xf6\xff\x89\xf8\x81,!\x1b\x08I\xc80\x04\
\x1ce\x01\xd9\x84\xd3l\xc1\x05$\xa3\x86\x1e\x09\x99\xe4\xe5>A\x11\x13\x93\
tkHA\xaa\xe1\x8e\xba\xaa\xee\xe1\xd6\xabW\xe5!"\x8f\xe8\xf2HH\x09)!\xff\
#d(\x14R\xa2\xd1\xe8]<\x1e\xb7u]\xa7D"\xf1c\xf1x\xcc\xb3"\x91\xc8\x0d\xd6\
\xf1\xfd\x1a$Lf\xc5b\x91\xea\xf5:\xb5Z-\xc72M\x93
\x85\x02\xc5b\xb1\xabo\xc2\xe0\xcfp\x05\x09\xc0e\xaf\xd7\xa3\xf1xL\xd3\
\xe9\xd4\xb1x^\xb7\xdbe\xd0\xe7}\x1eH\xfa\x14\xc9/\x11\xc8\xb9cHL\xf2s\x82\
n\x01\xb7A\x91\xa8\xfd\x99\x87\xa6i\x17\xb9\\\xee\xadR\xa9P6\x9bu\x0e\x99\
L&\xfd\xedv\xfb @\xd6d2\xa1F\xa3a\xefl\xaf\x0f%\xf0\xc0\xa5\xd4\xe9tVi\xe7\
\xf3\xf9\xbf\x85l6\x9b\x1b\xc8p8\x1c\xc0\xa1\x9a\x97\xcbeZ\x97R\xbf\xdf\
\x17\x07RU\xd5`*\x95ZT\xabU\x1a\x0c\x06\xab<F\x18\xc8t:\xadA\x16\x9f\xf8\
\xe1p\xb8\x01\x14\x06\x12\xed\xc8\xc6\x09?\xa9\xd5jO\x0c\xb8;F\x18H^\xd3\
0\x0c\x05\xdb\xfc\xb8\x9d\xa2P\xdb\xbd^\x17\xa0^@]n\xb76\xe1 \xd7B\xdb9\
\x03\xe8\xab\xd0\x90,\x94\x81>\x1a\x8d\xacC \xbd\x80\\\x1e\xa9\x99\xbf\xec\
\xf3\xc1\xbf |\x16\xae Y\xb8\x16gG\xba\x16\xaf\xbf\xf2)\x95J\x81L&\xa3\xba\
}`(\xb8\x15\xeead\xbb\x04\xb4P{\xb7h?>\xf92\x97\x90\x12RB~\xd4;[,X\xdf\x93\
y\xa9\x0b\x00\x00\x00\x00IEND\xaeB`\x82'''

    wx.MemoryFSHandler.AddFile('XRC/test_gui/test_gui_xrc', test_gui_xrc)
    wx.MemoryFSHandler.AddFile('XRC/test_gui/___img_icon_ico_cam_png', ___img_icon_ico_cam_png)
    __res.Load('memory:XRC/test_gui/test_gui_xrc')

