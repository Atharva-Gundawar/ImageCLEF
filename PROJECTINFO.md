# ImageCLEF 2015

>Deployment of model to classify images from the ImageCLEF 2015 dataset

## File Structure

```markdown
  ├── .gitignore                      
  ├── LICENSE                         
  ├── main.py                         
  ├── model                           
  │   ├── converted_keras             
  │   │   ├── keras_model.h5          
  │   │   └── labels.txt              
  │   └── converted_savedmodel        
  │       ├── labels.txt              
  │       └── model.savedmodel        
  │           ├── assets              
  │           └── saved_model.pb      
  ├── Model-zips                      
  │   ├── converted_keras.zip         
  │   └── converted_savedmodel.zip    
  ├── predict.py                      
  ├── PROJECTINFO.md                  
  ├── README.md                       
  └── requirements.txt                

```

## Contributing

1. Fork it (<https://github.com/Atharva-Gundawar/ImageCLEF>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
