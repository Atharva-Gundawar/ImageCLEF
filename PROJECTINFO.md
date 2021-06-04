
# ImageCLEF 2015

>Deployment of model to classify images from the ImageCLEF 2015 dataset

## File Structure

```markdown
  ├── .gitignore                      <- DSC
  ├── LICENSE                         <- DSC
  ├── main.py                         <- DSC
  ├── model                           <- DSC
  │   ├── converted_keras             <- DSC
  │   │   ├── keras_model.h5          <- DSC
  │   │   └── labels.txt              <- DSC
  │   └── converted_savedmodel        <- DSC
  │       ├── labels.txt              <- DSC
  │       └── model.savedmodel        <- DSC
  │           ├── assets              <- DSC
  │           └── saved_model.pb      <- DSC
  ├── Model-zips                      <- DSC
  │   ├── converted_keras.zip         <- DSC
  │   └── converted_savedmodel.zip    <- DSC
  ├── predict.py                      <- DSC
  ├── PROJECTINFO.md                  <- DSC
  ├── README.md                       <- DSC
  └── requirements.txt                <- DSC

```

## Contributing

1. Fork it (<https://github.com/Atharva-Gundawar/ImageCLEF>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
