# Analysing Lexical Ambiguity in Indic Machine Translation Systems

This project is my MTech Project at CDS IISc Bengaluru. The aim is to analyse wether the *patriarchial bias is amplied* or not by the *Indic MT models* while translating **ambiguous English relations**.

## Ambiguous English relations considered: 
- Grandmother
- Grandfather
- Aunt
- Uncle
- Sister-in-law
- Brother-in-law
- Niece
- Nephew
- Cousin

## Models considered: 
- IndicTrans2
- Sarvam AI
- Google Translate API
- Microsoft Phi
## Datasets Considered:
The training dataset is considered and found to be biased for patriarchial relations for the ambiguous English relations.

### BPCC 
<!-- ### BPCC  -->
<!-- 
draw tables with columns as languages (n total), rows as relations (n total) but each row has sub rows as patriarchy n matriachy. cells will have the values of no.of sentences translated/available in training set for that relation in that language. Fill with dummy value "000" for now-->

| Relation       | Hindi |  Odia | Bengali |  Marathi |  Gujarati |  Punjabi |  Tamil |  Telugu |  Kannada |  Malayalam | **Total** |
|----------------|-------|-------|---------|----------|-----------|----------|--------|---------|----------|------------| --------- |
| Grandmother (Patriarchy)    | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |  000 |
| Grandmother (Matriarchy)    | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |  000 |
| Grandfather (Patriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |
| Grandfather (Matriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |
| Aunt (Patriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |
| Aunt (Matriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |
| Uncle (Patriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |
| Uncle (Matriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |
| Sister-in-law (Patriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |
| Sister-in-law (Matriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |
| Brother-in-law (Patriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |
| Brother-in-law (Matriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |
| Niece (Patriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |
| Niece (Matriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |
| Nephew (Patriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |
| Nephew (Matriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |
| Cousin (Patriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 |
| Cousin (Matriarchy) | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 000 | |
| **Total** | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 | 000 000 | |



## Results

 *Amplied or not?*

## Next Steps:
- To check if amplied, next task is to collect English sentences with the ambiguos English words and translate them using various models. Check the count and ratio of patrirach vs matriarch translations.


--------
--------

 # Folder Structure
 1. BPCC_/extracted:
Since BPCC contains parallel sentences in separate folders with each file containing only one language, it was necessary to consolidate both languages into a single file with two columns. This approach facilitates visualization and improves accessibility for data frames.
This section contains sentence pairs arranged in two columns, derived from the training corpus of BPCC. These pairs are organized into respective folders based on languages.
<!-- table to show no.of sentences in each language? not needed laready must have been done by bpcc -->




 2. flores-22_dev, IN22_testset:
*Test Data for Evaluation:* 
The evaluation dataset for IndicTrans2 (AI4Bharat) includes folders for each language. 
<!-- Each folder contains two files: one with English sentences and the other with corresponding Indic sentences. -->


3. human_sent_train:
This dataset has been curated to include human-translated sentences utilized in the training of IndicTrans2. It comprises two folders:

     a. **extracted**: This directory includes pairs of sentences, with files organized by language and source.

     b. **filtered**: This directory contains only sentence pairs that include ambiguous words, with files organized by language.

4. **IndicTrans2**: The downloaded model.

5. **IndicTransToolkit**: A toolkit designed to assist with tokenization and other related tasks.

6. **Noto Sans Indic**: Fonts used to display Indic scripts.

7. **Old Code**: Contains test and trial code, notebooks, and data.

8. **Others**: During the translation process, certain words could not be classified as either patriarchal or matriarchal based on the collected ground truth. These words have been categorized under "Others." This folder is organized by language and ambiguous word, and it contains sentences featuring such ambiguous words.

9. **Pickle Files**: This directory contains length and data dictionaries, segregated by word and language.

10. **Relation Ground Data**: This directory stores the ground truth data for ambiguous relations, organized by language as collected from the annotators.

11. **Results**: This directory is designated for storing the results or graphical plots of various analyses and evaluations.

12. **Test CSV**: This directory contains CSV files with test data used for evaluating translation models.

13. **Trainset Filtered**: This directory includes filtered training data with ambiguous relations, organized by language.

14. **Translated CSV**: This directory holds CSV files with translated sentences from various models.


***NOTEBOOKS and other FILES***


15. `Analysing OTHERS.ipynb` : file to analyse OTHERS category
16. `Filtering_eng_relations.ipynb`: This notebook is used to filter sentences from the "extracted" directory and place them into the "filtered" directory. this file is very important. it is used to create the base line. this file considered the filtered sentences

17. `plot TEST set.ipynb`: This notebook is utilized to generate comparison graphs for test data across various models and languages. It requires the length dictionary from `Filtering_eng_relations.ipynb` [or similar file for test] and needs to be reviewed and refined for accurate plotting.

18. `plot_trainset.ipynb`: This notebook is utilized to generate comparison graphs for test data across various languages. It requires the length dictionary from `Filtering_eng_relations.ipynb`.

19. `possible_indic_relations.py`: This file contains the ground truth data structure, organized as a dictionary.
20. `TestSet_Pat_vs_Mat.ipynb`: This notebook contains code for evaluating various models using the test dataset to check the translation of ambiguous English relations in terms of patriarchal versus matriarchal bias.

21. `Test_Data_Gen.ipynb` : This notebook is used to generate test data for evaluation of the models. 

22. `test_sentences_eng.txt` : This file contains English sentences for the test data for evaluation of 4 models. Generated using `Test_Data_Gen.ipynb` by me.

23. TestSet_custom.ipynb : This notebook is used to test data (fetch translations of `test_sentences_eng.txt` from 4 models) for evaluation of the models. 

24. `resultant`: has the dataframe for keeping counts and plots
25. `others_res`: has the dataframe for keeping counts and plots for OTHERS category




 <!-- Corpus Name: wikimedia
     Package: wikimedia.en-hi in Moses format
     Website: http://opus.nlpl.eu/wikimedia-v20230407.php
     Release: v20230407
Release date: Thu Apr 13 09:40:02 EEST 2023
     License: <a href=https://creativecommons.org/licenses/by-sa/4.0/>CC–BY-SA 4.0</a></p>

This package is part of OPUS - the open collection of parallel corpora
OPUS Website: http://opus.nlpl.eu

Please <a href="http://opus.lingfil.uu.se/LREC2012.txt">cite the following article</a> if you use the OPUS packages and downloads in your own work:<br/> J. Tiedemann, 2012, <a href="http://www.lrec-conf.org/proceedings/lrec2012/pdf/463_Paper.pdf"><i>Parallel Data, Tools and Interfaces in OPUS.</i></a> In Proceedings of the 8th International Conference on Language Resources and Evaluation (LREC 2012)<br/>

Wikipedia translations published by the wikimedia foundation and their article translation system. The parallel data sets are published at https://dumps.wikimedia.org/other/contenttranslation NEW: additional sentence alignment to avoid long segments in translation units
 -->
