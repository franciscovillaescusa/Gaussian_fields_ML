In order to carry out the analysis first generate the 2D Gaussian density fields using the codes in data. For maps not affected by astrophysics effects use generate_fields.py

The code to train the network is main_maps.py. architecture.py and data.py contain the different architectures and the data handling, respectively.

For maps not affected by astrophysics, the dataset is called AstroNone. The architecture and value of the hyperparameters is in main_maps.py

The network performance can be tested using test_maps.py.

