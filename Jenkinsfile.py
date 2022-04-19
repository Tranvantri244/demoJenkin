pipeline{
	agent any
	stages{
		stage('Clone'){
			steps{
			git 'https://github.com/Tranvantri244/jenkin.git'
			}
		}
	}
}