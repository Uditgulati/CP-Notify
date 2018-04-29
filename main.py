#import scrapers.cf_scraper as cf
#import scrapers.cc_scraper as cc
import scrapers.spoj_scraper as spoj


#spoj.get_rank('uditgulati0')
#spoj.fetch_submissions()

ranks = spoj.fetch_ranks()
print(ranks)


#print(submissions)

#if __name__ == '__main__':
#	func()