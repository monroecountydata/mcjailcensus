from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
    DateTime,
    Date,
    Time,
    Boolean,
    Numeric,
    Unicode,
    )

#from sqlalchemy.types import (
#    CHAR,
#    VARCHAR,
#    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relation,
    )

Base = declarative_base()

class ScrapeRunModel(Base):
    __tablename__ = 'scraperuns'
    id= Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime)
    success = Column(Boolean)
    inmatecount = Column(Integer)
    bookingscount = Column(Integer)
    newinmates = Column(Integer)

    def __init__(self,datetime,success,inmatecount,bookingscount,newinmates):
        self.datetime = datetime
        self.success = success
        self.inmatecount = inmatecount
        self.bookingscount - bookingscount
        self.newinmates = newinmates

class InmateModel(Base):
    __tablename__ = 'inmates'
    id = Column(Integer, primary_key=True, index=True)
    first = Column(Unicode(64), index=True)
    last = Column(Unicode(64), index=True)
    middle = Column(Unicode(1), index=True)
    mcid = Column(Unicode(16), index=True)
    sex = Column(Unicode(1), index=True)
    race = Column(Unicode(1), index=True)
    dob = Column(Date, index=True)

    def __init__(self,first=None,last=None,middle=None,mcid=None,sex=None,race=None,dob=None):
        self.first = first
        self.last = last
        self.middle = middle
        self.mcid = mcid
        self.sex = sex
        self.race = race
        self.dob = dob

    def populated(self):
        pop = False
        if (self.first != None and 
            self.last != None and
            self.middle != None and
            self.mcid != None and
            self.sex != None and
            self.race != None and
            self.dob != None
           ):
            pop = True
        return pop

class CustodyModel(Base):
    __tablename__ = 'custodies'
    id = Column(Integer, primary_key=True, index=True)
    inmateid = Column(Integer, ForeignKey('inmates.id'))
    inmate = relation("InmateModel", backref="custodies")
    datetime = Column(DateTime)
    custodyclass = Column(Unicode(64), index=True)

    def __init__(self,inmate=None,datetime=None,custodyclass=None):
        self.inmate = inmate
        self.datetime = datetime
        self.custodyclass = custodyclass

    def populated():
        pop = False
        if (self.inmate != None and
            self.custodydate != None and
            self.custodytime != None and
            self.custodyclass != None
           ):
            pop = True
        return pop

class JudgeModel(Base):
    __tablename__ = 'judges'
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(Unicode(256), index=True)
    first = Column(Unicode(64), index=True)
    middle = Column(Unicode(64), index=True)
    last = Column(Unicode(64), index=True)

    def __init__(self,fullname,first,middle,last):
        self.fullname = fullname
        self.first = first
        self.middle = middle
        self.last = last

class CourtModel(Base):
    __tablename__ = 'courts'
    id = Column(Integer, primary_key=True, index=True)
    shortname = Column(Unicode(4), index=True)
    fullname = Column(Unicode(256), index=True)
    description = Column(Text)

    def __init__(self,shortname):
        self.shortname = shortname
        #self.fullname = fullname
        #self.description = description

class AgencyModel(Base):
    __tablename__ = 'agencies'
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(Unicode(256), index=True)
    description = Column(Text)

    def __init__(self,fullname):
        self.fullname = fullname
        #self.description = description

class ArrestTypeModel(Base):
    __tablename__ = 'arresttypes'
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(Unicode(256), index=True)
    description = Column(Text)

    def __init__(self,fullname):
        self.fullname = fullname
        #self.description = description

class ChargeModel(Base):
    __tablename__ = 'charges'
    id = Column(Integer, primary_key = True, index=True)
    fullname = Column(Unicode(256),index=True)
    description = Column(Text)

    def __init__(self,fullname):
        self.fullname = fullname
        #self.description = description

class BookingTypeModel(Base):
    __tablename__ = 'bookingtypes'
    id = Column(Integer, primary_key = True, index=True)
    fullname = Column(Unicode(256),index=True)
    description = Column(Text)

    def __init__(self,fullname):
        self.fullname = fullname
        #self.description = description

class CustodyTypeModel(Base):
    __tablename__ = 'custodytypes'
    id = Column(Integer, primary_key = True, index=True)
    shortname = Column(Unicode(8),index=True)
    fullname = Column(Unicode(256),index=True)
    description = Column(Text)

    def __init__(self,shortname):
        self.shortname = shortname
        #self.fullname = fullname
        #self.description = description

class BookingModel(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, index=True)

    inmateid = Column(Integer,ForeignKey('inmates.id'))
    inmate = relation('InmateModel', backref='inmates')

    scraperunid = Column(Integer,ForeignKey('scraperuns.id'))
    scraperun = relation('ScrapeRunModel',backref='bookings')

    courtid = Column(Integer,ForeignKey('courts.id'))
    court = relation('CourtModel',backref='bookings')

    judgeid = Column(Integer,ForeignKey('judges.id'))
    judge = relation('JudgeModel',backref='bookings')

    agencyid = Column(Integer,ForeignKey('agencies.id'))
    agency = relation('AgencyModel',backref='bookings')

    chargeid = Column(Integer,ForeignKey('charges.id'))
    charge = relation('ChargeModel',backref='bookings')

    arresttypeid = Column(Integer,ForeignKey('arresttypes.id'))
    arresttype = relation('ArrestTypeModel',backref='bookings')

    bookingtypeid = Column(Integer,ForeignKey('bookingtypes.id'))
    bookingtype = relation('BookingTypeModel',backref='bookings')

    custodytypeid = Column(Integer,ForeignKey('custodytypes.id'))
    custodytype = relation('CustodyTypeModel',backref='bookings')

    censusdate = Column(Date, index=True)
    datetime = Column(DateTime, index=True)
    bail = Column(Numeric, index=True)
    bond = Column(Numeric, index=True)
    expectedrelease = Column(DateTime, index=True)
    roc = Column(Unicode(128), index=True)
    indict = Column(Unicode(256), index=True)
    adjusteddate = Column(Date, index=True)
    term = Column(Integer, index=True)

    def __init__(self,
                 inmateid=None,
                 scraperunid=None,
                 courtid=None,
                 judgeid=None,
                 agencyid=None,
                 chargeid=None,
                 arresttypeid=None,
                 censusdate=None,
                 bookingdatetime=None,
                 bail=None,
                 bond=None,
                 expectedrelease=None,
                 roc=None,
                 indict=None,
                 adjustdate=None,
                 term=None
                ):
        self.inmateid = inmateid
        self.scraperunid = scraperunid
        self.courtid = courtid
        self.judgeid = judgeid
        self.agencyid = agencyid
        self.chargeid = chargeid
        self.arresttypeid = arresttypeid
        self.censusdate = censusdate
        self.bookingdatetime = bookingdatetime
        self.bail = bail
        self.bond = bond
        self.expectedrelease = expectedrelease
        self.roc = roc
        self.indict = indict
        self.adjustdate = adjustdate
        self.term = term

