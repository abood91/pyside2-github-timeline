import sys
from datetime import datetime

from PySide2.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
QGridLayout, QLabel, QLineEdit, QPushButton, QApplication, QFrame, QSizePolicy, QScrollArea)

from PySide2.QtCore import (QRect, QSize, Qt)

from PySide2.QtGui import (QIcon)


from styles import Main_Style, App_Constants, find_data_file

from gapi import github_api


data = []

monthNames = [
  "January", "February", "March", "April", "May", "June", "July", 
  "August", "September", "October", "November", "December" ]

class MainUI(QMainWindow):

    def __init__(self):
        '''
        default initializer for pyside2 application

            Parameters:
                    self: An object of a class

            Returns:
                    None
        '''
        self.github_api = github_api()
        QMainWindow.__init__(self)
        
        self.setupUI()

        # Shows the application as maximized window
        self.showMaximized()


    def setupUI(self):
        '''
        Setups the UI elements

            Parameters:
                    self: An object of a class

            Returns:
                    None
        '''

        # Sets the application icon to github icon
        app_icon = QIcon()
        app_icon.addFile(find_data_file('resources/giticon.svg'), QSize(16,16))
        app_icon.addFile(find_data_file('resources/giticon.svg'), QSize(24,24))
        app_icon.addFile(find_data_file('resources/giticon.svg'), QSize(32,32))
        app_icon.addFile(find_data_file('resources/giticon.svg'), QSize(48,48))
        app_icon.addFile(find_data_file('resources/giticon.svg'), QSize(256,256))
        app_icon.addFile(find_data_file('resources/giticon.svg'), QSize(512,512))
        self.setWindowIcon(app_icon)

        self.startSize = QSize(App_Constants.app_start_width, App_Constants.app_start_height)
        self.resize(self.startSize)
        self.setMinimumSize(self.startSize)
        self.setStyleSheet(Main_Style.mainwindow_standard)

        self.setWindowTitle(App_Constants.app_name)

        self.centralWidget = QWidget(self)

        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)

        self.frame_main = QFrame(self)
        self.frame_main.setObjectName(u"frame_main")

        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.frame_main.setStyleSheet(Main_Style.mainwindow_standard)

        self.frame_main.setSizePolicy(sizePolicy)


        self.main_frame_vertical_layout = QVBoxLayout(self.frame_main)
        self.main_frame_vertical_layout.setSpacing(0)
        self.main_frame_vertical_layout.setObjectName(u"main_frame_vertical_layout")
        self.main_frame_vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.frame_search = QFrame(self.frame_main)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setMinimumSize(self.frame_main.size())

        self.frame_search.setStyleSheet(Main_Style.frame_search)

        self.search_frame_vertical_layout = QVBoxLayout(self.frame_search)
        self.search_frame_vertical_layout.setSpacing(0)
        self.search_frame_vertical_layout.setObjectName(u"search_frame_vertical_layout")
        self.search_frame_vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.frame_search_box = QFrame(self.frame_search)
        self.frame_search_box.setObjectName(u"frame_search_box")

        self.search_horizontal_layout = QHBoxLayout(self.frame_search_box)
        self.search_horizontal_layout.setObjectName(u"search_horizontal_layout")
        self.search_horizontal_layout.setContentsMargins(10, 10, 10, 10)
        self.search_horizontal_layout.setSpacing(3)
        self.search_horizontal_layout.setAlignment(Qt.AlignCenter)


        self.frame_search_components = QFrame(self.frame_search_box)
        self.frame_search_components.setObjectName(u"frame_search_components")
        self.frame_search_components.setStyleSheet(Main_Style.frame_search_components)
        

        self.search_gridLayout = QGridLayout(self.frame_search_components)
        self.search_gridLayout.setObjectName(u"search_gridLayout")
        self.search_gridLayout.setContentsMargins(10, 10, 10, 10)
        self.search_gridLayout.setVerticalSpacing(3)
        self.search_gridLayout.setHorizontalSpacing(0)
        
        self.search_header_label = QLabel(self.frame_search_components)
        self.search_header_label.setObjectName(u"search_header_label")
        self.search_header_label.setStyleSheet(Main_Style.label_search_header)
        self.search_header_label.setText("Github Repo Timeline")
        self.search_header_label.setFixedSize(QSize(620, 80))
        self.search_gridLayout.addWidget(self.search_header_label, 0, 0, 1, 2, Qt.AlignLeft)

        self.search_label = QLabel(self.frame_search_components)
        self.search_label.setObjectName(u"search_label")
        self.search_label.setStyleSheet(Main_Style.label_search)
        self.search_label.setText("Enter username for a timeline")
        self.search_label.setFixedSize(QSize(620, 60))
        self.search_gridLayout.addWidget(self.search_label, 1, 0, 1, 2, Qt.AlignLeft)


        self.search_text = QLineEdit(self.frame_search_components)
        self.search_text.setObjectName(u"search_text")
        self.search_text.setFixedSize(QSize(460, 60))
        self.search_text.setStyleSheet(Main_Style.lineEdit_search)

        self.search_text.setPlaceholderText("Github Username...")
        
        self.search_gridLayout.addWidget(self.search_text, 2, 0, Qt.AlignRight)


        self.search_button = QPushButton(self.frame_search_components)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setFixedSize(QSize(160, 60))
        self.search_button.setStyleSheet(Main_Style.bt_search)
        search_button_Icon = QIcon()
        Icon_resource = find_data_file('resources/search.svg')
        search_button_Icon.addFile(Icon_resource, QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(search_button_Icon)
        self.search_button.setIconSize(QSize(20,20))
        self.search_button.setText(" Search")
        self.search_button.setCheckable(False)
        self.search_button.clicked.connect(lambda: self.search_button_click())
        
        self.search_gridLayout.addWidget(self.search_button, 2, 1, Qt.AlignLeft)

        self.search_horizontal_layout.addWidget(self.frame_search_components)

        self.search_frame_vertical_layout.addWidget(self.frame_search_box)

        self.main_frame_vertical_layout.addWidget(self.frame_search)


        self.frame_details = QFrame(self.frame_main)
        self.frame_details.setObjectName(u"frame_search")
        self.frame_details.setMinimumSize(self.frame_main.size())
        self.frame_details.setStyleSheet(Main_Style.frame_search)

        self.frame_details.setVisible(False)

        self.frame_details_vertical_layout = QVBoxLayout(self.frame_details)
        self.frame_details_vertical_layout.setSpacing(5)
        self.frame_details_vertical_layout.setObjectName(u"frame_details_vertical_layout")
        self.frame_details_vertical_layout.setAlignment(Qt.AlignHCenter)
        self.frame_details_vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.details_scrall_area = QScrollArea(self.frame_details)
        self.details_scrall_area.setObjectName(u"details_scrall_area")
        self.details_scrall_area.setStyleSheet(Main_Style.scroll_area)
        self.details_scrall_area.setFrameShape(QFrame.NoFrame)
        self.details_scrall_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.details_scrall_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.details_scrall_area.setWidgetResizable(True)
        
        self.details_scrall_area_widget_contents = QWidget()
        self.details_scrall_area_widget_contents.setObjectName(u"details_scrall_area_widget_contents")
        self.details_scrall_area_widget_contents.setStyleSheet("background-color:transparent;")
        self.details_scrall_area_widget_contents.setGeometry(QRect(0, 0, 
        int(App_Constants.app_start_width), int(App_Constants.app_start_height * 80)))

        self.details_vertical_layout = QVBoxLayout(self.details_scrall_area_widget_contents)
        self.details_vertical_layout.setAlignment(Qt.AlignCenter)
        self.details_vertical_layout.setObjectName(u"details_vertical_layout")
        self.details_scrall_area.setWidget(self.details_scrall_area_widget_contents)

        self.return_button = QPushButton(self.frame_details)
        self.return_button.setObjectName(u"return_button")
        self.return_button.setMinimumSize(QSize(300, 60))
        self.return_button.setMaximumHeight(60)
        self.return_button.setSizePolicy(sizePolicy)

        self.return_button.setStyleSheet(Main_Style.bt_search)
        self.return_button.setText(" Return to search ")
        self.return_button.setCheckable(False)
        self.return_button.clicked.connect(lambda: self.frames_toggle())

        self.frame_details_vertical_layout.addWidget(self.details_scrall_area)
        
        self.frame_details_vertical_layout.addWidget(self.return_button)
        
        self.main_frame_vertical_layout.addWidget(self.frame_details)
        

        # Create central widget's layout
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.frame_main)

        # set central widget layout
        self.centralWidget.setLayout(self.main_layout)
        # Set central widget
        self.setCentralWidget(self.centralWidget)
    
    
    def format_response(self, responses):
        '''
        Returns the a list of all the repos of the spcified user.

            Parameters:
                    self: An object of a class
                    username (json): json object to be formated

            Returns:
                    a responses dict that containes all the needed values. (repo name, repo cretion date)
        '''
        
        if responses != None and responses!=[]:
            repo_dict = []

            # First empty the details view
            self.empty_details_content()

            # Itterates throu the responce and adds items to the details view
            try:

                for item in responses:
                    dt = datetime.strptime(item['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                    repo_dict.append({'repo_id' : item['id'], 'name' : item['name'],
                    'date_time': dt.strftime('%Y.%m.%d %H:%M:%S'),
                    'dt': int(dt.strftime('%Y%m%d%H%M%S')),
                    'date' : {'year' : dt.year, 'month' : dt.month, 'day' : dt.day, 
                    'hour' : dt.hour, 'minute' : dt.minute, 'second' : dt.second}})
                

                repo_dict.sort(key=self.getKey)
                #print(repo_dict)

                for i in range(0, len(repo_dict)):

                    # initialize the counters

                    y = m = 0

                     # In case its the first item then add all item details
                    if i ==0:
                       
                        self.add_year(repo_dict[i]['date']['year'])
                        self.add_month(monthNames[int(repo_dict[i]['date']['month'])-1])
                        self.add_repo(repo_dict[i]['name'], repo_dict[i]['date_time'])
                    
                    # In case its not the first item, year of repo creation was not added previously 
                    # then adds all item details.
                    elif repo_dict[i]['date']['year'] != repo_dict[i-1]['date']['year']:
                        
                        m =0
                        y +=1
                        self.add_year(repo_dict[i]['date']['year'])
                        self.add_month(monthNames[int(repo_dict[i]['date']['month'])-1])
                        self.add_repo(repo_dict[i]['name'], repo_dict[i]['date_time'])

                    # In case its not the first item, year of repo creation was added previously 
                    # and the month was not added previously then adds the month and item details to the details view.
                    elif repo_dict[i]['date']['year'] == repo_dict[i-1]['date']['year'] and repo_dict[i]['date']['month'] != repo_dict[i-1]['date']['month']:
                        
                        m +=1
                        self.add_month(monthNames[int(repo_dict[i]['date']['month'])-1])
                        self.add_repo(repo_dict[i]['name'], repo_dict[i]['date_time'])
                    
                    # In case its not the first item, year of repo creation was added previously 
                    # and the month was added previously then adds only the item details to the details view.
                    elif repo_dict[i]['date']['year'] == repo_dict[i-1]['date']['year'] and repo_dict[i]['date']['month'] == repo_dict[i-1]['date']['month']:
                        self.add_repo(repo_dict[i]['name'], repo_dict[i]['date_time'])
                
                # toggle the details view and remove the search view
                self.frames_toggle()

                return repo_dict
            except Exception as exp:
                print(exp)
        else:
            print("responses was empty")

    def getKey(self, repo):
        '''
        Returns the value of a key of an object.

            Parameters:
                    self: An object of a class
                    repo (object): The key which contains the key

            Returns:
                    Returns the value of a key of an object
        '''
        return repo['dt']

    def search_button_click(self):

        res = self.github_api.make_request(self.search_text.text())
        self.format_response(res)


        


    def empty_details_content(self):
        '''
        empties the details conents

            Parameters:
                    self: An object of a class

            Returns:
                    None
        '''

        w = self.details_vertical_layout.takeAt(0)
        while w:
            w.widget().deleteLater()
            w = self.details_vertical_layout.takeAt(0)
        
        self.details_vertical_layout.update()


    def frames_toggle(self):
        '''
        toggles the view to show the search again

            Parameters:
                    self: An object of a class

            Returns:
                    None
        '''

        self.frame_details.setVisible(not self.frame_details.isVisible())
        self.frame_search.setVisible(not self.frame_search.isVisible())

    def add_year(self, year):
        '''
        Creates a year label and adds it to the details widget

            Parameters:
                    self: An object of a class
                    year (string): the year to be added

            Returns:
                    None
        '''

        year_label = QLabel(self.details_scrall_area_widget_contents)
        year_label.setObjectName(str(year)+u"year_label")
        year_label.setStyleSheet(Main_Style.year_label)
        year_label.setText(str(year))
        year_label.setFixedSize(QSize(200, 60))
        self.details_vertical_layout.addWidget(year_label)


    def add_month(self, month):
        '''
        Creates a month label and adds it to the details widget

            Parameters:
                    self: An object of a class
                    month (string): the month to be added

            Returns:
                    None
        '''

        month_label = QLabel(self.details_scrall_area_widget_contents)
        month_label.setObjectName(str(month)+u"month_label")
        month_label.setStyleSheet(Main_Style.month_label)
        month_label.setText(str(month))
        month_label.setFixedSize(QSize(200, 60))
        self.details_vertical_layout.addWidget(month_label)

    
    def add_repo(self, name, date):
        '''
        Creates a repo frame and labels and adds them to the details widget

            Parameters:
                    self: An object of a class
                    name (string): the repos name to be added
                    date (string): the date of the creation of the repos to be added

            Returns:
                    None
        '''

        repo_frame = QFrame(self.details_scrall_area_widget_contents)
        repo_frame.setObjectName(str(name)+u"_repo_frame")
        repo_frame.setStyleSheet(Main_Style.repo_frame)
        repo_frame.setMinimumSize(QSize(600, 200))
        repo_frame.setMaximumSize(QSize(600, 400))

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(repo_frame.sizePolicy().hasHeightForWidth())
        repo_frame.setSizePolicy(sizePolicy)

        sizePolicy_label = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy_label.setHorizontalStretch(1)
        sizePolicy_label.setVerticalStretch(1)
        

        repo_frame_horizontal_layout = QHBoxLayout(repo_frame)
        repo_frame_horizontal_layout.setObjectName(str(name)+u"_repo_frame_horizontal_layout")
        repo_frame_horizontal_layout.setContentsMargins(10, 10, 10, 10)
        repo_frame_horizontal_layout.setSpacing(2)
        repo_frame_horizontal_layout.setAlignment(Qt.AlignRight)

        repo_frame_content = QFrame(repo_frame)
        repo_frame_content.setObjectName(str(name)+u"repo_frame_content")
        repo_frame_content.setStyleSheet(Main_Style.repo_frame_content)
        repo_frame_content.setMinimumSize(QSize(400, 150))
        repo_frame_content.setMaximumSize(QSize(450, 250))
        repo_frame_content.setSizePolicy(sizePolicy)

        repo_frame_content_vertical_layout = QVBoxLayout(repo_frame_content)
        repo_frame_content_vertical_layout.setObjectName(str(name)+u"repo_frame_content_vertical_layout")
        repo_frame_content_vertical_layout.setContentsMargins(10, 10, 10, 10)
        repo_frame_content_vertical_layout.setSpacing(2)
        repo_frame_content_vertical_layout.setAlignment(Qt.AlignCenter)

        name_label = QLabel(repo_frame)
        name_label.setObjectName(str(name)+u"_repo_label")
        name_label.setStyleSheet(Main_Style.repo_label)
        name_label.setText(str(name))
        name_label.setAlignment(Qt.AlignLeft)
        name_label.setMinimumSize(QSize(300, 60))
        name_label.setMaximumSize(QSize(450, 60))
        name_label.setSizePolicy(sizePolicy_label)

        repo_frame_content_vertical_layout.addWidget(name_label)

        date_label = QLabel(repo_frame)
        date_label.setObjectName(str(name)+u"_repo_date_label")
        date_label.setStyleSheet(Main_Style.repo_date_label)
        date_label.setText(str(date))
        date_label.setMinimumSize(QSize(300, 60))
        date_label.setMaximumSize(QSize(450, 60))
        date_label.setSizePolicy(sizePolicy_label)
        date_label.setAlignment(Qt.AlignLeft)
        repo_frame_content_vertical_layout.addWidget(date_label)

        repo_frame_horizontal_layout.addWidget(repo_frame_content)

        self.details_vertical_layout.addWidget(repo_frame)

if __name__ == "__main__":

    # Exacutes the main functionality

    application = QApplication(sys.argv)
    mainWindow = MainUI()
    QApplication.processEvents()
    sys.exit(application.exec_())
