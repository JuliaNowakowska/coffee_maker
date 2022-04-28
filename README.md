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

## Implementation plan - milestones
1. GUI with intensity scale and additions checkboxes
2. Fuzzy logic model implementation
3. Success & error messages 
4. Saving output values to .csv
5. Evaluation

## Design
Project follows the colour palette: [colorhunt.co/palette/402218865439c68b59d7b19d](colorhunt.co/palette/402218865439c68b59d7b19d)

## Fuzzy logic model
The graphs below illustrate Mamdani logic model that is used in order to compute value of the output variable.
<img width="574" alt="Zrzut ekranu 2022-04-28 o 21 29 30" src="https://user-images.githubusercontent.com/45031945/165831754-c41de6a4-2cf4-4aa1-8b48-ae9322354d8b.png">

<img width="748" alt="Zrzut ekranu 2022-04-28 o 21 30 09" src="https://user-images.githubusercontent.com/45031945/165831798-f4c804a0-c9cf-4d00-856f-42a5ff1bec90.png">

<img width="748" alt="Zrzut ekranu 2022-04-28 o 21 30 14" src="https://user-images.githubusercontent.com/45031945/165831801-c28abd05-9d9b-4fec-bb16-fb2f5a0b85d4.png">

<img width="748" alt="Zrzut ekranu 2022-04-28 o 21 30 19" src="https://user-images.githubusercontent.com/45031945/165831816-05de7993-c32e-4618-ac3d-5ceed69d70be.png">

<img width="560" alt="Zrzut ekranu 2022-04-28 o 21 30 38" src="https://user-images.githubusercontent.com/45031945/165831828-8b92e51f-006e-41db-a99e-c644ef23bd9b.png">

<img width="560" alt="Zrzut ekranu 2022-04-28 o 21 30 57" src="https://user-images.githubusercontent.com/45031945/165831841-640de19b-2f62-492c-be7b-96502629ab4a.png">

<img width="571" alt="Zrzut ekranu 2022-04-28 o 21 31 35" src="https://user-images.githubusercontent.com/45031945/165831856-ea3db89e-c8f6-4e5a-8ed7-eea613d5dd00.png">

<img width="571" alt="Zrzut ekranu 2022-04-28 o 21 32 16" src="https://user-images.githubusercontent.com/45031945/165831864-3b84f69e-0c59-49d7-b10f-ab67d07a5bd9.png">

