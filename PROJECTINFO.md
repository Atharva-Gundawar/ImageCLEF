# Product Name
> Short blurb about what your product does.

### File Structure
------------
    ├── .gitignore
    ├── LICENSE
    ├── main.py
    ├── predict.py
    ├── PROJECTINFO.md
    ├── README.md
    ├── requirements.txt
    │
    ├───model
    │   ├───converted_keras
    │   │   ├──keras_model.h5
    │   │   └──labels.txt
    │   │
    │   └───converted_savedmodel
    │       ├── labels.txt
    │       └───model.savedmodel
    │           ├──saved_model.pb
    │           ├───assets
    │           └───variables
    │                ├──variables.data-00000-of-00001
    │                └──variables.index
    │
    └───Model-zips
        ├── converted_keras.zip
        └── converted_savedmodel.zip


--------

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
