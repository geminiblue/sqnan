<?php

/**
 * This is the model class for table "sq_clever".
 *
 * The followings are the available columns in table 'sq_clever':
 * @property integer $Id
 * @property string $Question
 * @property string $Answer
 */
class Clever extends CActiveRecord
{
	/**
	 * Returns the static model of the specified AR class.
	 * @param string $className active record class name.
	 * @return Clever the static model class
	 */
	public static function model($className=__CLASS__)
	{
		return parent::model($className);
	}

	/**
	 * @return string the associated database table name
	 */
	public function tableName()
	{
		return 'sq_clever';
	}

	/**
	 * @return array validation rules for model attributes.
	 */
	public function rules()
	{
		// NOTE: you should only define rules for those attributes that
		// will receive user inputs.
		return array(
			array('Question, Answer', 'safe'),
			// The following rule is used by search().
			// Please remove those attributes that should not be searched.
			array('Id, Question, Answer', 'safe', 'on'=>'search'),
		);
	}

	/**
	 * @return array relational rules.
	 */
	public function relations()
	{
		// NOTE: you may need to adjust the relation name and the related
		// class name for the relations automatically generated below.
		return array(
		);
	}

	/**
	 * @return array customized attribute labels (name=>label)
	 */
	public function attributeLabels()
	{
		return array(
			'Id' => 'ID',
			'Question' => 'Question',
			'Answer' => 'Answer',
		);
	}

	/**
	 * Retrieves a list of models based on the current search/filter conditions.
	 * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
	 */
	public function search()
	{
		// Warning: Please modify the following code to remove attributes that
		// should not be searched.

		$criteria=new CDbCriteria;

		$criteria->compare('Id',$this->Id);
		$criteria->compare('Question',$this->Question,true);
		$criteria->compare('Answer',$this->Answer,true);

		return new CActiveDataProvider($this, array(
			'criteria'=>$criteria,
		));
	}
}