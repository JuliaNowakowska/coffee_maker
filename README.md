# coffee_maker

## Project overview
Coffee Maker is a system that designs a perfect coffee. It receives information about the desired intensity and size of the coffee from the user and with fuzzy logic model returns amount of coffee beans that has to be used in order to prepare it. Furthermore, user can choose additions, like milk. 
<br><br>
The system could be used in coffee machines or in self-checkout systems in fast-food chains.

## Product requirements
### Business requirements
* user-friendly system
* accessibility - taking into account users with disabilities
* fuzzy logic model using "Golden Cup Standard"
* amount of water adjusted to cups sizes

### Technical requirements
* GUI
* correct fuzzy logic model - mamdani model
* possibility of downloading output values to .csv

## Target audience information
Users are customers who do not know and care much about the speciality coffee. They just want to drink it in the beginning of the day to gain some energy. The only thing they care about is customized intensity. They expect system to be fast and easy to use. 

## User journeys
1. First person wants to get a strong coffee that will give them a "kick". They approach the screen and see a 1 - 10 scale of desired intensity. They choose 10 and 25ml of water. Model returns a perfect espresso ingredients - 7g of coffee powder. 
2. Second user would like to buy americano. They choose "7" on intensity scale and 250ml of water. System returns variable value: coffee - 18g.
3. User would like to get a light coffee with milk. They choose "4" on the intensity scale, 300ml of water and additionally tick "milk" checkbox. System returns 9g of coffee and 50ml of milk. 

## Design
Project follows the colour palette: [colorhunt.co/palette/402218865439c68b59d7b19d](colorhunt.co/palette/402218865439c68b59d7b19d)

## Implementation plan - milestones
1. GUI with intensity scale and additions checkboxes
2. Fuzzy logic model implementation
3. Success & error messages 
4. Saving output values to .csv
5. Evaluation
