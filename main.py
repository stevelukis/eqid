"""
Latest Earthquake Detection Package
"""
import eqid

if __name__ == '__main__':
    result = eqid.get_data()
    eqid.console_print(result)
