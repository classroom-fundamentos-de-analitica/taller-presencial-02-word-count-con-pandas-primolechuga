"""Taller evaluable"""

import glob

import pandas as pd




def load_input(input_directory):
    """Load text files in 'input_directory/'"""

    filenames = glob.glob(input_directory + "/*.*")
    dataframes = [
        pd.read_csv(filename, sep="\t",names=['text']) for filename in filenames
    ]
    dataframe = pd.concat(dataframes).reset_index(drop=True)
    return dataframe



def clean_text(dataframe):
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #
    dataframe = dataframe.copy()
    dataframe['text'] = dataframe['text'].str.lower()
    dataframe['text'] = dataframe['text'].str.replace(",","").str.replace(".","")
    return dataframe



def count_words(dataframe):
    """Word count"""
    dataframe = dataframe.copy()
    dataframe['text'] = dataframe['text'].str.split()
    dataframe = dataframe.explode('text').reset_index(drop = True)
    dataframe = dataframe.rename(columns = {'text': 'word'})
    dataframe['count'] = 1
    conteo = dataframe.groupby(['word'], as_index= False).agg({'count' :sum})
    return conteo


def save_output(dataframe, output_filename):
    """Save output to a file."""
    dataframe.to_csv(output_filename, index = False,sep = "\t")


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions."""
    dataframe = load_input(input_directory)
    dataframe = clean_text(dataframe)
    dataframe = count_words(dataframe)
    dataframe = save_output(dataframe,"output.txt")



if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
