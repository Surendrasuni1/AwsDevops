








pipeline{
	agent{label 'master'}
		stages{
			stage('Clean workspace'){
				steps{
				  cleanWs()
				  }
			}	  
			stage('clone the source code'){
				steps{
					echo 'In SCM Stage'
					
					git credintialsId: 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbb', url: 'https://github.com/Surendrasuni1/sample', branch:'master'
				}	
		
			}
			stage('shell script'){
			    steps{
				   sh '''
				   
						pwd
						ls
						mkdir jen
						ls
				   
				   '''
				
				}
			}
		
		}




	}
