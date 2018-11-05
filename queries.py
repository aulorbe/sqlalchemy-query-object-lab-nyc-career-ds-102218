from sqlalchemy import create_engine, func
from seed import Company
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///dow_jones.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def return_apple(): # Write a query that returns a Apple's Company object.
    apple = session.query(Company).filter(Company.company=='Apple').first() # why do we do .first() here?
    return apple


## FIX TEST ERROR HERE
def return_disneys_industry(): # Write a query that returns Disney's industry.
    industry = session.query(Company).filter(Company.company=='Walt Disney').first()
    return industry



def return_list_of_company_objects_ordered_alphabetically_by_symbol(): #Write a query that returns a list of Company objects for all the companies in the Dow. The list should be ordered alphabetically by symbol.
    output = session.query(Company).order_by(Company.symbol).all()
    return output


#
def return_list_of_dicts_of_tech_company_names_and_their_EVs_ordered_by_EV_descending(): # Write a query that returns a list of dictionaries for all the technology companies in the DJIA. Each dictionary will have keys of 'company' and EV that point to the respective company name and enterprise value for each company. The list should be ordered by enterprise value from greatest to least.
    tech = session.query(Company).filter_by(industry='Technology').order_by(Company.enterprise_value.desc()) # explain difference between filter and filter_by()?
    arr = []
    for i in tech:
        obj = {'company': i.company, 'EV': i.enterprise_value}
        arr.append(obj)
    return arr



def return_list_of_consumer_products_companies_with_EV_above_225(): # Write a query that returns a those consumer products companies with an enterprise value over $225 billion. The query should return a list of dictionaries. Each dictionary will have a key of name that points to the company's full name.
    comps = session.query(Company).filter(Company.industry=='Consumer products',Company.enterprise_value > 225).all()

    output = []
    for i in comps:
        obj = {'name': i.company}
        output.append(obj)
    return output



def return_conglomerates_and_pharmaceutical_companies(): # Write a query that returns all companies in the conglomerates or pharmaceuticals industries. The query will return a list of all the company names that match this criteria.
    conglomerates = session.query(Company).filter_by(industry='Conglomerate').all()
    pharms = session.query(Company).filter_by(industry='Pharmaceuticals').all()

    conglo_names = []
    for i in conglomerates:
        conglo_names.append(i.company) # returns ['3M', 'General Electric', 'United Technologies']

    pharms_names = []
    for i in pharms:
        pharms_names.append(i.company) # returns ['Johnson & Johnson', 'Merck', 'Pfizer']

    return sorted(conglo_names + pharms_names)





def avg_EV_of_dow_companies(): #Write a query that calculates and returns the average enterprise value for a company in the Dow Jones Industrials.
    pass

def return_industry_and_its_total_EV(): # Write a query that returns each industry featured in the DJIA index and its respective total enterprise value. The resulting list will be ordered alphabetically by industry name.
    pass
