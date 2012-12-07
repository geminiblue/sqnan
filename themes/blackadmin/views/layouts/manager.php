<!DOCTYPE >
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Black Admin v2</title>
    <style type="text/css" media="all">
        @import url(<?php echo Yii::app()->theme->baseUrl?>/resources/css/style.css);
    </style>
    <script src="<?php echo Yii::app()->theme->baseUrl;?>/resources/js/jquery.js" type="text/javascript"></script>
    <script src="<?php echo Yii::app()->theme->baseUrl;?>/resources/js/jquery_ui.js" type="text/javascript"></script>
    <script src="<?php echo Yii::app()->theme->baseUrl;?>/resources/js/functions.js" type="text/javascript"></script>
</head>
<body>
<div id="container"> <!-- Container -->
    <div id="header"> <!-- Header -->
        <div id="title">
            Black Admin v2
            <span>Professional CMS Administrator Skin</span>
        </div>
        <div class="logged">
            <p>Good morning, <a href="#" title="">Administrator</a>!</p>
            <p><a href="#">My Account</a> | <a href="#" >Sign Out</a></p>
            <p>You have <a href="#">12 unred messages</a>!</p>
        </div>
    </div>
    <div id="sidebar"> <!-- Sidebar -->
        <div class="sidebox">
            <span class="stitle">控制面板</span>
            <div id="navigation"> <!-- Navigation begins here -->
                <div class="sidenav"><!-- Sidenav -->

                    <div class="navhead"><span>Articles</span></div>
                    <div class="subnav">
                        <ul class="submenu">
                            <li><a href="#" title="">Write a new Article</a></li>
                            <li><a href="#" title="">Manage Articles</a></li>
                            <li><a href="#" title="">Manage Comments</a></li>
                            <li><a href="#" title="">Manage Categories</a></li>
                        </ul>
                    </div>
                    <div class="navhead"><span>Events Calendar</span></div>
                    <div class="subnav">
                        <ul class="submenu">
                            <li><a href="#" title="">Submenu Item 1</a></li>
                            <li><a href="#" title="">Submenu Item 2</a></li>
                            <li><a href="#" title="">Submenu Item 3</a></li>
                        </ul>
                    </div>
                    <div class="navhead"><span>Pages</span></div>
                    <div class="subnav">
                        <ul class="submenu">
                            <li><a href="#" title="">Submenu Item 1</a></li>
                            <li><a href="#" title="">Submenu Item 2</a></li>
                            <li><a href="#" title="">Submenu Item 3</a></li>
                            <li><a href="#" title="">Submenu Item 4</a></li>
                        </ul>
                    </div>
                    <div class="navhead"><span>Image Gallery</span></div>
                    <div class="subnav">
                        <ul class="submenu">
                            <li><a href="#" title="">Submenu Item 1</a></li>
                            <li><a href="#" title="">Submenu Item 2</a></li>
                            <li><a href="#" title="">Submenu Item 3</a></li>
                        </ul>
                    </div>
                    <div class="navhead"><span>Settings</span></div>
                    <div class="subnav">
                        <ul class="submenu">
                            <li><a href="#" title="">Submenu Item 1</a></li>
                            <li><a href="#" title="">Submenu Item 2</a></li>
                            <li><a href="#" title="">Submenu Item 3</a></li>
                        </ul>
                    </div>
                </div>
            </div> <!-- END Navigation -->
        </div>
        <div class="sidebox">
            <span class="stitle">Sales information</span>
            <p><b>103 products</b> sold today.</p>
            <p><b>103 products</b> sold today.</p>
            <p><b>103 products</b> sold today.</p>
            <p><b>103 products</b> sold today.</p>
            <p><b>103 products</b> sold today.</p>
        </div>
    </div> <!-- END Sidebar -->
    <div id="main"> <!-- Main, right side content -->
        <div id="content"> <!-- Content begins here -->
        <?php echo $content;?>
        </div>
    </div>

    </div>
    <div id="footer">
        <p>Copyright <?php echo Yii::app()->name;?> 2009. All rights reserved.</p>
    </div>
</div>
</body>
</html>

