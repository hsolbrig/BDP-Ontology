SRC=model/schema/SourceDataModel.yaml
ARGS=--no-mergeimports
mkdir -p model/python
gen-python $ARGS --no-slots $SRC  > model/python/sourcedatamodel.py
mkdir -p model/docs
gen-markdown -d model/docs -i $ARGS $SRC
mkdir -p model/jsonld
gen-jsonld-context $ARGS $SRC > model/jsonld/SourceDataModel.context.json
