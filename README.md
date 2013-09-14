##mcjailcensus##


Tools for capturing, processing, saving, and viewing the Monroe County Jail System Census data


###Setup###

Pull down git repo:

    $ git clone https://github.com/monroecountydata/mcjailcensus.git
    
Install virtualenv:

    $ sudo apt-get install python-virtualenv

Create virtual enviornment:

    $ virtualenv --no-site-packages -p python2 hflosskenv
    $ . hflosskenv/bin/activate
    
Install needed packages:

    $ pip install beautifulsoup4
    $ pip install sqlalchemy
    $ pip install zope.sqlalchemy
    $ pip install pdfminer
    $ pip install transaction
   
    
###Running###

    $ python processcensus.py
   
  
###Output###

The script will generate three files:

    rawfile.txt
        This is the raw pdf2txt output (not pretty)
        
    pdftext.txt
        This is the 'pre-processed' pdf text (prettier, but not pretty)
        
    inmates.sqlite
        This is an SQLite3 database of all of the inmate, custody, and booking data found in the PDF
    
    
###Files###

    processcensus.py
        Big file with all of the functions to download, pre-process, and process the census pdf file.
        It also includes all of the code that pushes that data to a database via SQLAlchemy.
        
    models.py
        SQLAlchemy models for DB access.
    
    
###Notes###

- If you already have a inmates.sqlite file present in the same folder as the processcensus.py, it will not delete it, 
  but add to it.  This means that if you want to keep different runs separate, you should be renaming this file!

- within main() in processcensus.py there is a variable called DEBUG that is set to False.  When this is set to True
  the script will pull from pdftext.txt rather than pulling the latest PDF from the internet.  This is very useful for
  debugging the script since pdf2txt conversion takes almost a minute ...


###Disclamer###

This is in no way associated with or maintained by Monroe County, NY and is supplied "as is" with no warranty or 
guarantee to work or produce acurate information.
