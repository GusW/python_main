# scurri - Gustavo Watanabe (gustavo.watanabe@gmail.com)

### Tell us about one thing you are proud of in your career.
### It could be a difficult technical problem you had to solve in your work or a personal project.
### There is no need to go into details; a short paragraph explaining the problem and why you are proud of it would be fine.

While working for 2XT, we had an ambitious project which consisted in capturing web user info on the fly while they were searching for travel insurance offers in our web app. If they do not purchase any insurance within 15 minutes the system will trigger the phone system connecting automatically a salesperson to the final user. The salesperson is picked in a first-in, first-out algorithm and only valid phones will trigger a call. Salesperson has 30 seconds to decide if they are going to pick the client; if rejected they need to explain why. Salesperson keeps blocked if no explanation is provided. Every salesperson has a maximum of 2 attempts/contacts to sell the insurance and if this limit is reached the client returns to the queue for the next iteration. If 2 different salespersons can not sell that insurance the client is allocated in a Whatsapp/mailing list. If the client makes another search in our web app, the counters restart and its contact is again in the queue.

I had to integrate our Django with the third-party phone system, create a server queue in Golang and link with our Django API, develop a Chrome extension where salesperson could interact with, implement all business logic - the whole project was fairly complex, I had to acquire multiple technical skill in a short time. We could deploy the whole system and a couple of months later we noticed the company earnings were steadily increasing.
