import os, sys

RESOURCE_FOLDER_PATH = ''


def find_data_file(filename):
    '''
    returns the exact resouce location

        Parameters:
                filename (string): intended file name

        Returns:
                RESOURCE_FOLDER_PATH (string): the full path of the needed resource
    '''  
    if getattr(sys, "frozen", False):
        # The application is frozen
        RESOURCE_FOLDER_PATH = os.path.dirname(sys.executable)
    else:
        RESOURCE_FOLDER_PATH = os.path.dirname(os.path.realpath(__file__))
        # The application is not frozen
        # Change this bit to match where you store your data files:
        
    return (RESOURCE_FOLDER_PATH + os.path.sep + filename).replace("\\", "/")
    
class App_Constants():

    app_start_height = 1024
    app_start_width = 768


    app_name = "Github Timeline"

    if sys.platform == "darwin":
        app_start_height = 900
        app_start_width = 675

class Colors():
    
    transparent = " transparent; "
    dark_gray = " #24292d; "
    mid_gray = " #2b3137; "
    light_gray = " #bcc3ba; "
    primary = " #2fbb4f; "
    primary_hover = " #23d64d; "
    error = " #ff0000; "

class Main_Style():

    
    mainwindow_standard = (
    """
    QMainWindow {
        background-color:""" + Colors.dark_gray + """
    }

    QToolTip {
        color: #ffffff;
        background-color: rgba(27, 29, 35, 160);
        border: 1px solid rgb(40, 40, 40);
        border-radius: 2px;
    }
    """
    )

    frame_search = (

    """
    QFrame {
        background-image: url('./resources/github.svg');
        background-repeat: no-repeat;
        background-position: bottom right;
        width:100%;
        height:100%;
        margin: 0;
        padding: 0;
    }
    """
    )
    
    frame_search_components = (

    """
    QFrame {
        background: transparent;
        width:100%;
        height:100%;
        margin: 0;
        padding: 0;
    }
    """
    )
    

    bt_search = (
    """
    QPushButton, QPushButton[Active=true] {
        background-color: """ + Colors.primary + """
        border-top-right-radius: 5px;
        border-bottom-right-radius: 5px;
        font-size: 22px;
        color:white;
        
    }
    QPushButton:hover {
        background-color: """ + Colors.primary_hover + """
        
    }
    QPushButton:pressed {	
        background-color: """ + Colors.primary + """
    }
    """
    )

    
    lineEdit_search = (  
    """

    QLineEdit {
        background-color: white;
        border-top-left-radius: 5px;
        border-bottom-left-radius: 5px;
        font-size: 22px;
        padding-left: 10px;
    }
    """
    )

    label_search_header = (
    """
    QLabel {
        background-color: """ + Colors.transparent + """
        color: """ + Colors.primary + """
        font-size: 60px;
        font-weight:500;
        padding-left: 0px;

    }
    """
    )
        
    label_search = (
    """
    QLabel {
        background-color: """ + Colors.transparent + """
        color: white;
        font-size: 24px;
        font-weight:250;
        padding-left: 0px;

    }
    """
    )


    year_label = (
    """
    QLabel {
        color: """ + Colors.light_gray + """
        font-size: 60px;
        font-weight:400;
        padding-left: 0px;

    }
    """
    )


    month_label = (
    """
    QLabel {
        color: """ + Colors.light_gray + """
        font-size: 30px;
        font-weight:250;

    }
    """
    )

    repo_label = (
    """
    QLabel {
        color: """ + Colors.dark_gray + """
        font-size: 28px;
        font-weight:300;

    }
    """
    )

    repo_date_label = (
    """
    QLabel {
        color: """ + Colors.light_gray + """
        font-size: 18px;
        font-weight:150;

    }
    """
    )

    repo_frame = (

    """
    QFrame {
        background: """ + Colors.transparent + """
    }
    """
    )

    
    repo_frame_content = (

    """
    QFrame {
        background: white;
        border-radius: 10px;
        margin: 0;
        padding: 10;
    }
    """
    )

    scroll_area = (
    """
    QScrollArea {
        background: """ + Colors.transparent + """
    }
    
    QScrollBar:horizontal {
        border: none;
        background: """ + Colors.transparent + """
    }
    QScrollBar:vertical {
        border: none;
        background: """ + Colors.transparent + """
    }
    """
    )


