import xarray as xr

class DataReader:
    def __init__(self, file_path):
        """Initialize DataReader with file path.
        
        Args:
            file_path (str): Path to the data file
        """
        self.file_path = file_path
        self.data = None
        
    def read_data(self):
        """Read data from file using xarray.
        
        Returns:
            xarray.Dataset: Loaded dataset
        """
        try:
            self.data = xr.open_dataset(self.file_path)
            return self.data
        except Exception as e:
            raise Exception(f"Error reading file {self.file_path}: {str(e)}")
            
    def close(self):
        """Close the dataset if it's open."""
        if self.data is not None:
            self.data.close()
            self.data = None