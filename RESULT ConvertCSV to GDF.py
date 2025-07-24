Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py
Traceback (most recent call last):
  File "C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py", line 6, in <module>
    df = pd.read_csv("facilities.csv")
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1880, in _make_engine
    self.handles = get_handle(
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 873, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'facilities.csv'

= RESTART: C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py
Traceback (most recent call last):
  File "C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py", line 6, in <module>
    df = pd.read_csv(r"C:\Users\User\Documents\2025 Master UiTM\Sem 1\GES 716 Programming\SLIDE\INDIVIDUAL PROJECT\Test Koordinat Kedai.csv")
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1898, in _make_engine
    return mapping[engine](f, **self.options)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 93, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 574, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 663, in pandas._libs.parsers.TextReader._get_header
  File "pandas/_libs/parsers.pyx", line 874, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas/_libs/parsers.pyx", line 891, in pandas._libs.parsers.TextReader._check_tokenize_status
  File "pandas/_libs/parsers.pyx", line 2053, in pandas._libs.parsers.raise_parser_error
  File "<frozen codecs>", line 325, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x92 in position 150: invalid start byte

================ RESTART: C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py ================
Traceback (most recent call last):
  File "C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py", line 6, in <module>
    df = pd.read_csv(r"C:\Users\User\Documents\2025 Master UiTM\Sem 1\GES 716 Programming\SLIDE\INDIVIDUAL PROJECT\Test Koordinat Kedai.csv")
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1898, in _make_engine
    return mapping[engine](f, **self.options)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 93, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 574, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 663, in pandas._libs.parsers.TextReader._get_header
  File "pandas/_libs/parsers.pyx", line 874, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas/_libs/parsers.pyx", line 891, in pandas._libs.parsers.TextReader._check_tokenize_status
  File "pandas/_libs/parsers.pyx", line 2053, in pandas._libs.parsers.raise_parser_error
  File "<frozen codecs>", line 325, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x92 in position 150: invalid start byte

================ RESTART: C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py ================
Traceback (most recent call last):
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7096, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'longitude'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py", line 9, in <module>
    geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 4107, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3819, in get_loc
    raise KeyError(key) from err
KeyError: 'longitude'

================ RESTART: C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py ================
Traceback (most recent call last):
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7096, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'longitude'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py", line 9, in <module>
    geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 4107, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3819, in get_loc
    raise KeyError(key) from err
KeyError: 'longitude'

================ RESTART: C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py ================
Traceback (most recent call last):
  File "C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py", line 7, in <module>
    df = pd.read_csv(file_path)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1898, in _make_engine
    return mapping[engine](f, **self.options)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 93, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 574, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 663, in pandas._libs.parsers.TextReader._get_header
  File "pandas/_libs/parsers.pyx", line 874, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas/_libs/parsers.pyx", line 891, in pandas._libs.parsers.TextReader._check_tokenize_status
  File "pandas/_libs/parsers.pyx", line 2053, in pandas._libs.parsers.raise_parser_error
  File "<frozen codecs>", line 325, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x92 in position 150: invalid start byte
>>> 
================ RESTART: C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py ================
Traceback (most recent call last):
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7096, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'longitude'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py", line 9, in <module>
    geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 4107, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3819, in get_loc
    raise KeyError(key) from err
KeyError: 'longitude'

= RESTART: C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py
   NO                               NAME  ...   longitude                   geometry
0   1             Damascus Bukit Bintang  ...  101.711824   POINT (101.71182 3.1475)
1   2              Halab Gate Restaurant  ...  101.710835  POINT (101.71084 3.14791)
2   3  Kunafa Crisp (or Kunafa Fingers)  ...  101.711299   POINT (101.7113 3.14744)
3   4                            Zaitoun  ...  101.711443  POINT (101.71144 3.14573)
4   5                       Friend Fries  ...  101.712002    POINT (101.712 3.14775)

[5 rows x 5 columns]

= RESTART: C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/ConvertCSV to GDF.py
   NO                               NAME  latitude   longitude  \
0   1             Damascus Bukit Bintang  3.147498  101.711824   
1   2              Halab Gate Restaurant  3.147911  101.710835   
2   3  Kunafa Crisp (or Kunafa Fingers)  3.147442  101.711299   
3   4                            Zaitoun  3.145730  101.711443   
4   5                       Friend Fries  3.147754  101.712002   

                    geometry  
0   POINT (101.71182 3.1475)  
1  POINT (101.71084 3.14791)  
2   POINT (101.7113 3.14744)  
3  POINT (101.71144 3.14573)  
4    POINT (101.712 3.14775)  

= RESTART: C:/Users/User/Documents/2025 Master UiTM/Sem 1/GES 716 Programming/SLIDE/INDIVIDUAL PROJECT/app.py
2025-07-23 14:29:53.937 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-07-23 14:29:54.196 WARNING streamlit: 
  [33m[1mWarning:[0m to view a Streamlit app on a browser, use Streamlit in a file and
  run it with the following command:

    streamlit run [FILE_NAME] [ARGUMENTS]
2025-07-23 14:29:54.211 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-07-23 14:29:54.220 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-07-23 14:29:54.230 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-07-23 14:29:54.239 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-07-23 14:29:54.249 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
