# Suspected Lung Cancer Example
This directory contains the various resources needed to demonstrate the "ISOSemantic" model of Suspected Lung Cancer, which
was the textbook example for Stan Huff's CIMI initiative.

## Notes on SNOMED CT and OWL
To convert the complete SNOMED CT into OWL:
1) Download https://github.com/IHTSDO/snomed-owl-toolkit/releases/download/3.0.3/snomed-owl-toolkit-3.0.3-executable.jar
2) Using the instructions on https://github.com/IHTSDO/snomed-owl-toolkit:
   1) java -jar snomed-owl-toolkit-3.0.3-executable.jar -rf2-to-owl -rf2-snapshot-archives SnomedCT_InternationalRF2_PRODUCTION_20210731T120000Z.zip

This produces a file in the form `ontology-2021-08-04_12-14-31.owl`
## Contents
```
  + --- README.md:     this file
  |
  + --- schema         LinkML Schema for the three isosemantic models
  |       |
  |       + --- IsoSemanticModel.yaml       LinkML model for the three different forms
  |
  + --- SNOMED         SNOMED Subset needed for reasoning over the isosemantic models
          |
          + --- README.md       Description of how the SNOMED Subset was created
          |
          + --- conf.json       Configuration file for SNOMEDToOWL conversion
          |
          + --- Subset          Transitive neighborhood of SNOMED CT "Suspected Lung Cancer" concepts
                  |
                  + --- Refset        RF2 representation of SNOMED CT subset focused around [162573006 |Suspected lung cancer (situation)|](http://snomed.info/id/162573006)
                  |
                  + --- SuspectedLungCancer.ttl    OWL representation of SCT subset
```

## Process
### Generating the SNOMED CT subset
1) Download and unzip the [latest SNOMED CT International Version](https://www.nlm.nih.gov/healthit/snomedct/index.html)
2) Install the [SNOMEDToOWL package](https://github.com/hsolbrig/SNOMEDCTToOWL)
    ```bash
    > mkdir sctto_venv
    > cd sctto_venv
    > touch Pipfile
    > pipenv install SNOMEDToOWL
    > pipenv shell
    (SNOMEDCTToOWL) 
    ```
3) Extract the transitive neighborhood of [162573006 |Suspected lung cancer (situation)|](http://snomed.info/id/162573006)
   ```bash
   (SNOMEDCTToOWL) > cd BDP-Ontology/SuspectedLungCancer/SNOMED
   (SNOMEDCTToOWL) > RF2Filter -i -a -d SnomedCT_InternationalRF2_PRODUCTION_20210731T120000Z/Snapshot Subset 162573006
   Build transitive closure list
   Processing SnomedCT_InternationalRF2_PRODUCTION_20210731T120000Z/Snapshot/Terminology/sct2_Relationship_Snapshot_INT_20210731.txt
   Filtering files
   Processing SnomedCT_InternationalRF2_PRODUCTION_20210731T120000Z/Snapshot/Terminology/sct2_Relationship_Snapshot_INT_20210731.txt
   Iteration 1: 53 new concepts
   Processing SnomedCT_InternationalRF2_PRODUCTION_20210731T120000Z/Snapshot/Terminology/sct2_Relationship_Snapshot_INT_20210731.txt
   Iteration 2: 104 new concepts
   Processing SnomedCT_InternationalRF2_PRODUCTION_20210731T120000Z/Snapshot/Terminology/sct2_Relationship_Snapshot_INT_20210731.txt
   Iteration 3: 37 new concepts
   Processing SnomedCT_InternationalRF2_PRODUCTION_20210731T120000Z/Snapshot/Terminology/sct2_Relationship_Snapshot_INT_20210731.txt
   Iteration 4: 5 new concepts
   Processing SnomedCT_InternationalRF2_PRODUCTION_20210731T120000Z/Snapshot/Terminology/sct2_Relationship_Snapshot_INT_20210731.txt
   Adding 363 concepts
   Processing SnomedCT_InternationalRF2_PRODUCTION_20210731T120000Z/Snapshot/Terminology/sct2_Concept_Snapshot_INT_20210731.txt
   Processing SnomedCT_InternationalRF2_PRODUCTION_20210731T120000Z/Snapshot/Terminology/sct2_Description_Snapshot-en_INT_20210731.txt
   Processing SnomedCT_InternationalRF2_PRODUCTION_20210731T120000Z/Snapshot/Terminology/sct2_TextDefinition_Snapshot-en_INT_20210731.txt
   Processing SnomedCT_InternationalRF2_PRODUCTION_20210731T120000Z/Snapshot/Refset/Language/der2_cRefset_LanguageSnapshot-en_INT_20210731.txt
   Processing SnomedCT_InternationalRF2_PRODUCTION_20210731T120000Z/Snapshot/Terminology/sct2_sRefset_OWLExpressionSnapshot_INT_20210731.txt 
   (SNOMEDCTToOWL) >
   ```
4) Convert the resulting RF2 files into OWL
   ```bash
   (SNOMEDCTToOWL) > SNOMEDToOWL Subset conf.json -o SuspectedLungCancer.ttl
   Creating transitive relationships
   Processing RF2 files
   Processing der2_cRefset_LanguageSnapshot-en_INT_20210731.txt
   Processing sct2_Relationship_Snapshot_INT_20210731.txt
   Processing sct2_Concept_Snapshot_INT_20210731.txt
   Processing sct2_Description_Snapshot-en_INT_20210731.txt
   Processing sct2_TextDefinition_Snapshot-en_INT_20210731.txt
   Generating OWL concepts
   Generating OWL properties
   Adding localized descriptions
   Writing SuspectedLungCancer.ttl
   Summary:
       Concepts: 301
       Definitions: 0
       Equivalentclass: 52
       Labels: 301
       Prefnames: 180
       Propchains: 1
       Properties: 134
       Rolegreoups: 0
       Subclassof: 139
       Synonyms: 0
       Ungrouped: 0
   (SNOMEDCTToOWL) >
   ```
5) Load SuspectedLungCancer.ttl into Protege, classify it, and save the classified results in OWL functional syntax
We used the Fact++ reasoner.  The export function is in file / Export inferred axioms as ontology ...
   * Select ALL options to export
   * Include annotations
   * Include asserted logical axioms
   * Set Ontology IRI to http://ontologies-r.us/bdp/snomed/suspectedlungcancer
   * Save to BDP-Ontology/SuspectedLungCancer/SNOMED/SuspectedLungCancer.owl
   * Export to OWL Functional Syntax
