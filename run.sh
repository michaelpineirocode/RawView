cd server && gcloud builds submit --tag gcr.io/photo-viewer-622f7/flask-fire
afplay /System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Resources/Sounds/Alert.aiff
cd .. && gcloud beta run deploy --image gcr.io/photo-viewer-622f7/flask-fire
firebase deploy