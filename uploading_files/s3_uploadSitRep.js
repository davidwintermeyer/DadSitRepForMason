/**
 * Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * This file is licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License. A copy of
 * the License is located at
 *
 * http://aws.amazon.com/apache2.0/
 *
 * This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
 * CONDITIONS OF ANY KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations under the License.
 */

//snippet-sourcedescription:[s3_PhotoExample.js demonstrates how to manipulate photos in albums stored in an Amazon S3 bucket.]
//snippet-service:[s3]
//snippet-keyword:[JavaScript]
//snippet-sourcesyntax:[javascript]
//snippet-keyword:[Code Sample]
//snippet-keyword:[Amazon S3]
//snippet-sourcetype:[full-example]
//snippet-sourcedate:[]
//snippet-sourceauthor:[AWS-JSDG]

// ABOUT THIS NODE.JS SAMPLE: This sample is part of the SDK for JavaScript Developer Guide topic at
// https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-example-photo-album.html

// snippet-start:[s3.JavaScript.photoAlbumExample.complete]
// snippet-start:[s3.JavaScript.photoAlbumExample.config]
var albumBucketName = "dadsitrepformason-public.com";
var bucketRegion = "us-east-1";
var IdentityPoolId = "us-east-1:af4f2e31-154d-4897-8646-44580544a597";
var sitRepFolder = 'uploadedSitReps'

AWS.config.update({
  region: bucketRegion,
  credentials: new AWS.CognitoIdentityCredentials({
    IdentityPoolId: IdentityPoolId
  })
});

var s3 = new AWS.S3({
  apiVersion: "2006-03-01",
  params: { Bucket: albumBucketName }
});
// snippet-end:[s3.JavaScript.photoAlbumExample.config]

// I'm leaving this with the S3 objects even though I don't care about it at all.
function uploadSitRepEntryPoint() {
  s3.listObjects({ Delimiter: "/" }, function(err, data) {
    if (err) {
      return alert("There was an error listing your albums: " + err.message);
    } else {
      var htmlTemplate = [
        '<p>Select the sitrep to upload using the *Choose File* button, then click uploadSitRep',
        '<br>',
        '<br>',
        '<input id="sitrepupload" type="file" accept="application/*">',
        "<button onclick=\"uploadSitRep()\">",
        "Upload Sit Rep",
        "</button>"
      ];
      document.getElementById("app").innerHTML = getHtml(htmlTemplate);
    }
  });
}

//// snippet-start:[s3.JavaScript.uploadSitRepEntryPoint]
//function uploadSitRepEntryPoint() {
//  var htmlTemplate = [
//    "<h2>Upload Button</h2>",
//    "Click the button to upload the sitrep",
//    // https://stackoverflow.com/questions/11832930/html-input-file-accept-attribute-file-type-csv
//    '<input id="sitrepupload" type="file" accept="application/*">',
//    "<button onclick=\"uploadSitRep(prompt('Upload Sit Rep:'))\">",
//    "Upload Sit Rep",
//    "</button>"
//  ];
//  document.getElementById("app").innerHTML = getHtml(htmlTemplate);
//}
//// snippet-end:[s3.JavaScript.uploadSitRepEntryPoint]

// snippet-start:[s3.JavaScript.uploadSitRep]
function uploadSitRep() {
  var files = document.getElementById("sitrepupload").files;
  if (!files.length) {
    return alert("Please choose a file to upload first.");
  }
  var file = files[0];
  var fileName = file.name;
  var folderKey = encodeURIComponent(sitRepFolder) + "/";

  var sitRepKey = folderKey + fileName;

  // Use S3 ManagedUpload class as it supports multipart uploads
  var upload = new AWS.S3.ManagedUpload({
    params: {
      Bucket: albumBucketName,
      Key: sitRepKey,
      Body: file
    }
  });

  var promise = upload.promise();

  promise.then(
    function(data) {
      alert("Successfully uploaded sitrep photo.");
    },
    function(err) {
      // TODO: Have an alart on this
      return alert("There was an error uploading the sitrep: ", err.message);
    }
  );
}
// snippet-end:[s3.JavaScript.uploadSitRep]

// snippet-end:[s3.JavaScript.photoAlbumExample.complete]