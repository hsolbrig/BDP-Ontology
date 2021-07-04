# BDP-Ontology

Refer to Approach.md for detailed information.


# Background


**Ontology and OWL Tutorial:**

https://www.cs.cornell.edu/courses/cs431/2008sp/Lectures/public/lecture-4-09-08.pdf


**Where to Download Protegé:**

https://protege.stanford.edu/


**Intro to RDF:**

https://www.w3.org/TR/rdf11-primer/


**3 Papers related to our project:**

**Previous approaches:**

https://www.w3.org/TR/swbp-specified-values/

https://www.cs.man.ac.uk/~rector/papers/Terminology-binding-final-revision-embedded-single-rector%20copy.pdf

**Most recent approach (we're trying to enhance this):**

https://www.cs.man.ac.uk/~rector/papers/Whats-in-a-code/Whats-in-a-code-rector-corrected.pdf



**Blending RDF and OWL**

Github: https://github.com/BD2KOnFHIR/BLENDINGFHIRandRDF <br>
Paper: https://jhu.pure.elsevier.com/en/publications/blending-fhir-rdf-and-owl

**Using Z: Specification, Refinement and Proof**

PDF: http://www.usingz.com/usingz.pdf

&nbsp; &nbsp; &nbsp; &nbsp; See section __4.4 Definite description__

<br>
<br>

# TODO (6/18/2021 ~ 6/27/2021)


## 1. Download

Copy of NCIT
https://evs.nci.nih.gov/ftp1/NCI_Thesaurus/
<br>
A: "Thesaurus.OWL.zip"<br>
AND<br>
B: "ThesaurusInf_21.05d.OWL.zip"

## 2. Load B into Protege and examine structures, be familiar with Protege. 
Load A and run reasoner. It should give same thing as B.

## 3. Download

Copy of SNOMED-CT

https://www.nlm.nih.gov/healthit/snomedct/index.html

To do this, you have to sign-up, get license (if needed), and download international release in rf2 format.

## 4. Download 

https://github.com/IHTSDO/classification-service

Then, use this to convert rf2 to owl format.

## 5. Get reasoner plugin ELK and Snorocket

ELK can be downloaded by File>Check for plugin

Snorocket install

https://aehrc.com/snorocket/

This line _should_ be crossed out:~~Go to the Maven Central Repository and download the latest as snorocket-protege-4.0.1-jar-with-dependencies.jar and then copy it into Protege-5.5.0/Protege.app/Contents/Java/plugins~~

Update: Protege5.5.0 is not compatible either the snorocket 3.2.0 release nor snorocket 4.0.1.  We have to switch back to Protege 5.2 and snorocket 3.2:

* Download Protege 5.2.0 from the bottom of page: https://github.com/protegeproject/protege-distribution/releases/tag/v5.2.0, then unzip and (optionally) move
Protege-5.2.0/Protégé.app to /Applications.  (Mac OSX Only)
* Download Snorocket from https://search.maven.org/remotecontent?filepath=au/csiro/snorocket-protege/3.2.0/snorocket-protege-3.2.0-jar-with-dependencies.jar and
copy it into Protégé.app/Contents/Java/plugins

## 6. Change Memory Setting 

This line should be crossed out: edit ~~Protege-5.5.0/Protégé.app/Contents/Info.plist~~

edit Protege-5.2.0/Protégé.app/Contents/Info.plist
```

<array>
            <string>-Dapple.laf.useScreenMenuBar=true</string>
            <string>-Xss16M</string>
            <string>-Xmx8G</string>
            <string>-Xdock:name=Protégé</string>
            <string>-DentityExpansionLimit=100000000</string>
            <string>-Dlogback.configurationFile=conf/logback.xml</string>
            <string>-Dfile.encoding=UTF-8</string>
            <string>-XX:CompileCommand=exclude,javax/swing/text/GlyphView,getBreakSpot</string>
        </array>
```

The element with "-Xmx" in it - change the current setting to "-Xmx8G"   -- this is assuming that your machine has at least 8GB of memory.
        
        

## 7. Read 

Mondo Paper

## 8. Read 

through background stuff more to familarize with concepts like equivalent class, subclass, protege...

## 9. Read 

through BlendingFHIRandRDF tutorial.




