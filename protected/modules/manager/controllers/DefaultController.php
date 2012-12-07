<?php

class DefaultController extends Controller
{
    public $layout='//layouts/manager';
	public function actionIndex()
	{
		$this->render('index');
	}
}