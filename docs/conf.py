# -*- coding: utf-8 -*-
#
# Pathomx documentation build configuration file, created by
# sphinx-quickstart on Thu Dec 12 15:30:39 2013.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

class MockType(type):

    def __init__(self, *args, **kwargs):
        super(MockType, self).__init__(*args)
        
    def __call__(self, *args, **kwargs):
        return self
        
    getSaveFileName = None
    SizeAllCursor = None
    PointingHandCursor = None
    ArrowCursor = None
    CrossCursor = None

    Key_Control = 'control'
    Key_Shift = 'shift'
    Key_Alt = 'alt'
    Key_Meta = 'super'
    Key_Return = 'enter'
    Key_Left = 'left'
    Key_Up = 'up'
    Key_Right = 'right'
    Key_Down = 'down'
    Key_Escape = 'escape'
    Key_F1 = 'f1'
    Key_F2 = 'f2'
    Key_F3 = 'f3'
    Key_F4 = 'f4'
    Key_F5 = 'f5'
    Key_F6 = 'f6'
    Key_F7 = 'f7'
    Key_F8 = 'f8'
    Key_F9 = 'f9'
    Key_F10 = 'f10'
    Key_F11 = 'f11'
    Key_F12 = 'f12'
    Key_Home = 'home'
    Key_End = 'end'
    Key_PageUp = 'pageup'
    Key_PageDown = 'pagedown'

    MetaModifier = None
    AltModifier = None
    ControlModifier = None
    LeftButton = None
    RightButton = None
    MidButton = None
    
    start_event_loop_default = None
    stop_event_loop_default = None
    
    
class Mock(object):
    __all__ = [
        'QAbstractOpenGLFunctions', 'QAbstractTextDocumentLayout', 'QActionEvent', 'QBackingStore', 'QBitmap', 'QBrush', 'QClipboard', 'QCloseEvent', 'QColor', 'QConicalGradient', 'QContextMenuEvent', 'QCursor', 'QDesktopServices', 'QDoubleValidator', 'QDrag', 'QDragEnterEvent', 'QDragLeaveEvent', 'QDragMoveEvent', 'QDropEvent', 'QEnterEvent', 'QExposeEvent', 'QFileOpenEvent', 'QFocusEvent', 'QFont', 'QFontDatabase', 'QFontInfo', 'QFontMetrics', 'QFontMetricsF', 'QGlyphRun', 'QGradient', 'QGuiApplication', 'QHelpEvent', 'QHideEvent', 'QHoverEvent', 'QIcon', 'QIconDragEvent', 'QIconEngine', 'QImage', 'QImageIOHandler', 'QImageReader', 'QImageWriter', 'QInputEvent', 'QInputMethod', 'QInputMethodEvent', 'QInputMethodQueryEvent', 'QIntValidator', 'QKeyEvent', 'QKeySequence', 'QLinearGradient', 'QMatrix2x2', 'QMatrix2x3', 'QMatrix2x4', 'QMatrix3x2', 'QMatrix3x3', 'QMatrix3x4', 'QMatrix4x2', 'QMatrix4x3', 'QMatrix4x4', 'QMouseEvent', 'QMoveEvent', 'QMovie', 'QOffscreenSurface', 'QOpenGLBuffer', 'QOpenGLContext', 'QOpenGLContextGroup', 'QOpenGLDebugLogger', 'QOpenGLDebugMessage', 'QOpenGLFramebufferObject', 'QOpenGLFramebufferObjectFormat', 'QOpenGLPaintDevice', 'QOpenGLShader', 'QOpenGLShaderProgram', 'QOpenGLTimeMonitor', 'QOpenGLTimerQuery', 'QOpenGLVersionProfile', 'QOpenGLVertexArrayObject', 'QPagedPaintDevice', 'QPaintDevice', 'QPaintEngine', 'QPaintEngineState', 'QPaintEvent', 'QPainter', 'QPainterPath', 'QPainterPathStroker', 'QPalette', 'QPdfWriter', 'QPen', 'QPicture', 'QPictureIO', 'QPixmap', 'QPixmapCache', 'QPolygon', 'QPolygonF', 'QQuaternion', 'QRadialGradient', 'QRawFont', 'QRegExpValidator', 'QRegion', 'QRegularExpressionValidator', 'QResizeEvent', 'QScreen', 'QScrollEvent', 'QScrollPrepareEvent', 'QSessionManager', 'QShortcutEvent', 'QShowEvent', 'QStandardItem', 'QStandardItemModel', 'QStaticText', 'QStatusTipEvent', 'QStyleHints', 'QSurface', 'QSurfaceFormat', 'QSyntaxHighlighter', 'QTabletEvent', 'QTextBlock', 'QTextBlockFormat', 'QTextBlockGroup', 'QTextBlockUserData', 'QTextCharFormat', 'QTextCursor', 'QTextDocument', 'QTextDocumentFragment', 'QTextDocumentWriter', 'QTextFormat', 'QTextFragment', 'QTextFrame', 'QTextFrameFormat', 'QTextImageFormat', 'QTextInlineObject', 'QTextItem', 'QTextLayout', 'QTextLength', 'QTextLine', 'QTextList', 'QTextListFormat', 'QTextObject', 'QTextObjectInterface', 'QTextOption', 'QTextTable', 'QTextTableCell', 'QTextTableCellFormat', 'QTextTableFormat', 'QTouchDevice', 'QTouchEvent', 'QTransform', 'QValidator', 'QVector2D', 'QVector3D', 'QVector4D', 'QWhatsThisClickedEvent', 'QWheelEvent', 'QWindow', 'QWindowStateChangeEvent', 'qAlpha', 'qBlue', 'qFuzzyCompare', 'qGray', 'qGreen', 'qIsGray', 'qRed', 'qRgb', 'qRgba',
        'QAbstractButton', 'QAbstractGraphicsShapeItem', 'QAbstractItemDelegate', 'QAbstractItemView', 'QAbstractScrollArea', 'QAbstractSlider', 'QAbstractSpinBox', 'QAction', 'QActionGroup', 'QApplication', 'QBoxLayout', 'QButtonGroup', 'QCalendarWidget', 'QCheckBox', 'QColorDialog', 'QColumnView', 'QComboBox', 'QCommandLinkButton', 'QCommonStyle', 'QCompleter', 'QDataWidgetMapper', 'QDateEdit', 'QDateTimeEdit', 'QDesktopWidget', 'QDial', 'QDialog', 'QDialogButtonBox', 'QDirModel', 'QDockWidget', 'QDoubleSpinBox', 'QErrorMessage', 'QFileDialog', 'QFileIconProvider', 'QFileSystemModel', 'QFocusFrame', 'QFontComboBox', 'QFontDialog', 'QFormLayout', 'QFrame', 'QGesture', 'QGestureEvent', 'QGestureRecognizer', 'QGraphicsAnchor', 'QGraphicsAnchorLayout', 'QGraphicsBlurEffect', 'QGraphicsColorizeEffect', 'QGraphicsDropShadowEffect', 'QGraphicsEffect', 'QGraphicsEllipseItem', 'QGraphicsGridLayout', 'QGraphicsItem', 'QGraphicsItemGroup', 'QGraphicsLayout', 'QGraphicsLayoutItem', 'QGraphicsLineItem', 'QGraphicsLinearLayout', 'QGraphicsObject', 'QGraphicsOpacityEffect', 'QGraphicsPathItem', 'QGraphicsPixmapItem', 'QGraphicsPolygonItem', 'QGraphicsProxyWidget', 'QGraphicsRectItem', 'QGraphicsRotation', 'QGraphicsScale', 'QGraphicsScene', 'QGraphicsSceneContextMenuEvent', 'QGraphicsSceneDragDropEvent', 'QGraphicsSceneEvent', 'QGraphicsSceneHelpEvent', 'QGraphicsSceneHoverEvent', 'QGraphicsSceneMouseEvent', 'QGraphicsSceneMoveEvent', 'QGraphicsSceneResizeEvent', 'QGraphicsSceneWheelEvent', 'QGraphicsSimpleTextItem', 'QGraphicsTextItem', 'QGraphicsTransform', 'QGraphicsView', 'QGraphicsWidget', 'QGridLayout', 'QGroupBox', 'QHBoxLayout', 'QHeaderView', 'QInputDialog', 'QItemDelegate', 'QItemEditorCreatorBase', 'QItemEditorFactory', 'QKeyEventTransition', 'QLCDNumber', 'QLabel', 'QLayout', 'QLayoutItem', 'QLineEdit', 'QListView', 'QListWidget', 'QListWidgetItem', 'QMainWindow', 'QMdiArea', 'QMdiSubWindow', 'QMenu', 'QMenuBar', 'QMessageBox', 'QMouseEventTransition', 'QPanGesture', 'QPinchGesture', 'QPlainTextDocumentLayout', 'QPlainTextEdit', 'QProgressBar', 'QProgressDialog', 'QPushButton', 'QRadioButton', 'QRubberBand', 'QScrollArea', 'QScrollBar', 'QScroller', 'QScrollerProperties', 'QShortcut', 'QSizeGrip', 'QSizePolicy', 'QSlider', 'QSpacerItem', 'QSpinBox', 'QSplashScreen', 'QSplitter', 'QSplitterHandle', 'QStackedLayout', 'QStackedWidget', 'QStatusBar', 'QStyle', 'QStyleFactory', 'QStyleHintReturn', 'QStyleHintReturnMask', 'QStyleHintReturnVariant', 'QStyleOption', 'QStyleOptionButton', 'QStyleOptionComboBox', 'QStyleOptionComplex', 'QStyleOptionDockWidget', 'QStyleOptionFocusRect', 'QStyleOptionFrame', 'QStyleOptionGraphicsItem', 'QStyleOptionGroupBox', 'QStyleOptionHeader', 'QStyleOptionMenuItem', 'QStyleOptionProgressBar', 'QStyleOptionRubberBand', 'QStyleOptionSizeGrip', 'QStyleOptionSlider', 'QStyleOptionSpinBox', 'QStyleOptionTab', 'QStyleOptionTabBarBase', 'QStyleOptionTabWidgetFrame', 'QStyleOptionTitleBar', 'QStyleOptionToolBar', 'QStyleOptionToolBox', 'QStyleOptionToolButton', 'QStyleOptionViewItem', 'QStylePainter', 'QStyledItemDelegate', 'QSwipeGesture', 'QSystemTrayIcon', 'QTabBar', 'QTabWidget', 'QTableView', 'QTableWidget', 'QTableWidgetItem', 'QTableWidgetSelectionRange', 'QTapAndHoldGesture', 'QTapGesture', 'QTextBrowser', 'QTextEdit', 'QTimeEdit', 'QToolBar', 'QToolBox', 'QToolButton', 'QToolTip', 'QTreeView', 'QTreeWidget', 'QTreeWidgetItem', 'QTreeWidgetItemIterator', 'QUndoCommand', 'QUndoGroup', 'QUndoStack', 'QUndoView', 'QVBoxLayout', 'QWhatsThis', 'QWidget', 'QWidgetAction', 'QWidgetItem', 'QWizard', 'QWizardPage', 'qApp', 'qDrawBorderPixmap', 'qDrawPlainRect', 'qDrawShadeLine', 'qDrawShadePanel', 'qDrawShadeRect', 'qDrawWinButton', 'qDrawWinPanel',
        'QAbstractAnimation', 'QAbstractEventDispatcher', 'QAbstractItemModel', 'QAbstractListModel', 'QAbstractNativeEventFilter', 'QAbstractProxyModel', 'QAbstractState', 'QAbstractTableModel', 'QAbstractTransition', 'QAnimationGroup', 'QBasicTimer', 'QBitArray', 'QBuffer', 'QByteArray', 'QByteArrayMatcher', 'QChildEvent', 'QCoreApplication', 'QCryptographicHash', 'QDataStream', 'QDate', 'QDateTime', 'QDir', 'QDirIterator', 'QDynamicPropertyChangeEvent', 'QEasingCurve', 'QElapsedTimer', 'QEvent', 'QEventLoop', 'QEventLoopLocker', 'QEventTransition', 'QFile', 'QFileDevice', 'QFileInfo', 'QFileSystemWatcher', 'QFinalState', 'QGenericArgument', 'QGenericReturnArgument', 'QHistoryState', 'QIODevice', 'QIdentityProxyModel', 'QItemSelection', 'QItemSelectionModel', 'QItemSelectionRange', 'QLibrary', 'QLibraryInfo', 'QLine', 'QLineF', 'QLocale', 'QLockFile', 'QMargins', 'QMessageAuthenticationCode', 'QMessageLogContext', 'QMessageLogger', 'QMetaClassInfo', 'QMetaEnum', 'QMetaMethod', 'QMetaObject', 'QMetaProperty', 'QMetaType', 'QMimeData', 'QMimeDatabase', 'QMimeType', 'QModelIndex', 'QMutex', 'QMutexLocker', 'QObject', 'QObjectCleanupHandler', 'QParallelAnimationGroup', 'QPauseAnimation', 'QPersistentModelIndex', 'QPluginLoader', 'QPoint', 'QPointF', 'QProcess', 'QProcessEnvironment', 'QPropertyAnimation', 'QReadLocker', 'QReadWriteLock', 'QRect', 'QRectF', 'QRegExp', 'QRegularExpression', 'QRegularExpressionMatch', 'QRegularExpressionMatchIterator', 'QResource', 'QRunnable', 'QSaveFile', 'QSemaphore', 'QSequentialAnimationGroup', 'QSettings', 'QSharedMemory', 'QSignalMapper', 'QSignalTransition', 'QSize', 'QSizeF', 'QSocketNotifier', 'QSortFilterProxyModel', 'QStandardPaths', 'QState', 'QStateMachine', 'QStringListModel', 'QSysInfo', 'QSystemSemaphore', 'QT_TRANSLATE_NOOP', 'QT_TR_NOOP', 'QT_TR_NOOP_UTF8', 'QT_VERSION', 'QT_VERSION_STR', 'QTemporaryDir', 'QTemporaryFile', 'QTextBoundaryFinder', 'QTextCodec', 'QTextDecoder', 'QTextEncoder', 'QTextStream', 'QTextStreamManipulator', 'QThread', 'QThreadPool', 'QTime', 'QTimeLine', 'QTimer', 'QTimerEvent', 'QTranslator', 'QUrl', 'QUrlQuery', 'QUuid', 'QVariant', 'QVariantAnimation', 'QWaitCondition', 'QWriteLocker', 'QXmlStreamAttribute', 'QXmlStreamAttributes', 'QXmlStreamEntityDeclaration', 'QXmlStreamEntityResolver', 'QXmlStreamNamespaceDeclaration', 'QXmlStreamNotationDeclaration', 'QXmlStreamReader', 'QXmlStreamWriter', 'Q_ARG', 'Q_CLASSINFO', 'Q_ENUMS', 'Q_FLAGS', 'Q_RETURN_ARG', 'Qt', 'QtCriticalMsg', 'QtDebugMsg', 'QtFatalMsg', 'QtMsgType', 'QtSystemMsg', 'QtWarningMsg','pyqtBoundSignal', 'pyqtPickleProtocol', 'pyqtProperty', 'pyqtRemoveInputHook', 'pyqtRestoreInputHook', 'pyqtSetPickleProtocol', 'pyqtSignal', 'pyqtSlot', 'pyqtWrapperType', 'qAbs', 'qAddPostRoutine', 'qAddPreRoutine', 'qChecksum', 'qCompress', 'qCritical', 'qDebug', 'qErrnoWarning', 'qFatal', 'qFuzzyCompare', 'qInf', 'qInstallMessageHandler', 'qIsFinite', 'qIsInf', 'qIsNaN', 'qIsNull', 'qQNaN', 'qRegisterResourceData', 'qRemovePostRoutine', 'qRound', 'qRound64', 'qSNaN', 'qSetFieldWidth', 'qSetMessagePattern', 'qSetPadChar', 'qSetRealNumberPrecision', 'qSharedBuild', 'qUncompress', 'qUnregisterResourceData', 'qVersion', 'qWarning', 'qrand', 'qsrand', 'reset', 'right', 'scientific', 'showbase', 'uppercasebase', 'uppercasedigits', 'ws',
        'Figure', 'QFileDialog', 'QWebPage', 'QWebView', 'IPlugin', 'Engine',
    ]

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return Mock()
  
    @classmethod
    def __getattr__(cls, name):
        if name in ('__file__', '__path__'):
            return '/dev/null'
        elif name[0] == name[0].upper():
            mockType = MockType(name, (), {})
            mockType.__module__ = __name__
            mockType.__all__ = [] 
            return mockType
        else:
            return Mock()

MOCK_MODULES = [
        'PyQt5',
        'PyQt5.QtGui',
        'PyQt5.QtCore',
        'PyQt5.QtWebKit',
        'PyQt5.QtNetwork',
        'PyQt5.QtWidgets',
        'PyQt5.QtWebKitWidgets',
        'PyQt5.QtPrintSupport',
        'numpy',
        'scipy',
        'nmrglue',
        'gpml2svg',
        'poster.encode',
        'wheezy.template',
        'sklearn',
        'sklearn.decomposition',
        'icoshift',
        'nmrglue.fileio.fileiobase',
        'matplotlib',
        'matplotlib.backends',
        'matplotlib.backends.backend_agg',
        'matplotlib.figure',
        'matplotlib.backend_bases',
        'matplotlib._pylab_helpers',
        'matplotlib.widgets',
        'matplotlib.cbook',
        'matplotlib.colors',
        'matplotlib.cm',
        'dateutil',
        'yapsy',
        'yapsy.IPlugin',
        'yapsy.PluginManager',
        'wheezy',
        'wheezy.template',
        'wheezy.template.engine',
        'wheezy.template.ext',
        'wheezy.template.ext.core',
        'wheezy.template.ext.code',
        'wheezy.template.loader',
        ]

for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = Mock()
    
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
#sys.path.insert(0, os.path.abspath('../pathomx') )
sys.path.insert(0, os.path.abspath('..') )

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc','sphinx.ext.viewcode']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Pathomx'
copyright = u'2013, Martin A. Fitzpatrick, Catherine M. McGrath, Stephen P. Young'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.9'

# The full version, including alpha/beta/rc tags.
release = '2.2.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Pathomxdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'Pathomx.tex', u'Pathomx Documentation',
   u'Martin A. Fitzpatrick, Catherine M. McGrath, Stephen P. Young', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'pathomx', u'Pathomx Documentation',
     [u'Martin A. Fitzpatrick, Catherine M. McGrath, Stephen P. Young'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'Pathomx', u'Pathomx Documentation',
   u'Martin A. Fitzpatrick, Catherine M. McGrath, Stephen P. Young', 'Pathomx', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False
