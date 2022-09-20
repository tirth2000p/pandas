import NLP_Blackbox
import pandas as pd
import pathlib

formats = ['.xlsx', '.xlsm', '.xlsb', '.xltx', '.xltm', '.xls', '.xlt', '.xls', '.xml', '.xml', '.xlam', '.xla', '.xlw', '.xlr']

def data_ext(filename):
    ext = pathlib.Path(filename).suffix
    if ext in formats:
        try:
            df = pd.read_excel(filename)
            C1 = df[df.columns[0]].tolist()
            C2 = df[df.columns[1]].tolist()
            C3 = df[df.columns[2]].tolist()
            C4 = df[df.columns[3]].tolist()
            C5 = []
            C6 = []

            ##      loop go through list C4 pass each one to NLP as text    ##
            ## NLP will return with a flag of pass/fail/review and a reason ##

            for x in C4:

                tp=NLP_Blackbox.bx()

                ## to be replaced by Pass, Fail or Review flag from NLP ##
                C5.append(tp[0])

                ## Need to provide reason from NLP ##
                C6.append(tp[1])



            # Adding column named flag
            df['Flag'] = C5



            # Adding column named Reason
            df['Reason'] = C6
            print('pass')
            return df

        except:
            return 'Fail'


if __name__ == '__main__':
    data_ext()
