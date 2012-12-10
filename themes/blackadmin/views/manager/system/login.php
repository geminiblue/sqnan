<!DOCTYPE >
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>Black Admin v2</title>
        <link href="<?php echo Yii::app()->theme->baseUrl?>/resources/css/login.css" type="text/css" rel="stylesheet"/>
	</head>
<body>
	<div id="container">
		<h1>游离博客</h1>
		<div id="box">
<?php $form=$this->beginWidget('CActiveForm', array(
	'id'=>'login-form',
	'enableClientValidation'=>true,
	'clientOptions'=>array(
		'validateOnSubmit'=>true,
	),
)); ?>			
			<p class="main">
				<label>Username: </label>
				<?php echo $form->textField($model,'username'); ?>
				<label>Password: </label>
				<?php echo $form->passwordField($model,'password'); ?>
			</p>
			<p class="space">
				<span><input type="checkbox" />Remember me</span>
				<input type="submit" value="Login" class="login" />
			</p>
<?php $this->endWidget(); ?>
		</div>
	</div>
</body>
</html>