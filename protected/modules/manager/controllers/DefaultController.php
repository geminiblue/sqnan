<?php

class DefaultController extends Controller
{
	public function filters()
	{
		return array(
			'accessControl', // perform access control for CRUD operations
			//'postOnly + delete', // we only allow deletion via POST request
		);
	}
	/**
	 * Specifies the access control rules.
	 * This method is used by the 'accessControl' filter.
	 * @return array access control rules
	 */
	public function accessRules()
	{
		return array(

			
			array('allow', // allow authenticated user to perform 'create' and 'update' actions
				'actions'=>array('create','update','list','index','delete','admin','list','view'),
				'users'=>array('@'),
			),
			array('deny',  // allow all users to perform 'index' and 'view' actions
					'users'=>array('*'),
			),
			/*
			array('allow', // allow admin user to perform 'admin' and 'delete' actions
				'actions'=>array('admin','delete'),
				'users'=>array('admin'),
			),
			array('deny',  // deny all users
				'users'=>array('*'),
			),
			*/
		);
	}
	public function actionIndex()
	{
		$this->renderPartial('index');
	}
	public function actionLogin()
	{

	}
	public function actionLoginOut()
	{

	}
}