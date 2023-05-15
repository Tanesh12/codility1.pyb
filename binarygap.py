<!DOCTYPE html>
<!-- saved from url=(0050)https://app.codility.com/c/run/trainingR4ZZZF-PJE/ -->
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  
<link rel="apple-touch-icon" sizes="180x180" href="https://app.codility.com/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="https://app.codility.com/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="https://app.codility.com/favicon-16x16.png">
<link rel="manifest" href="https://app.codility.com/site.webmanifest">
<link rel="mask-icon" href="https://app.codility.com/safari-pinned-tab.svg" color="#1B6994">
<meta name="theme-color" content="#1B6994">

  









<title>

  Codility

</title>




<link rel="stylesheet" href="./binarygap_files/css">
<link rel="stylesheet" href="./binarygap_files/css(1)">
<link rel="stylesheet" href="./binarygap_files/icon">

<script type="application/json" id="data-bag-raven">{"dsn": "https://3c62a8dced574696a68571c03fbc875c@sentry.codility.net/11", "user": {"is_recruiter": false, "is_programmer": true, "id": 1022943, "username": "taneshpurohit7@gmail.com", "email": "taneshpurohit7@gmail.com", "is_superuser": false}}</script><script src="./binarygap_files/raven.auto.js.download" nonce=""></script><script src="./binarygap_files/123df631d9350b8941b3.8341.js.download"></script><script src="./binarygap_files/8404efb79fc84f97388c.raven.js.download"></script>
<script nonce="">window.config = {"csrfToken": "HEgRtNYBT4mXo2GjeqVlclYL94uKQjIQJcGn8mxli5bvL6cBzVXkMCxM7otzGQuk", "supportEmail": "support@codility.com", "upgradeEmail": "upgrades@codility.com", "collaborateUrl": "https://app.codility.com/services/codelive/collaborate/", "staticUrl": "/static/", "isRecruiter": false, "cacheId": "a56e3406b9b56cfe0d170cbb7660a2da4dee8f51", "logRocketId": "codility/frontend-jzrmw", "pendo": {"projectApiKey": "c6ae7399-061a-4c96-677e-4dca765e00f5", "includeUserPII": true, "site": "US"}};</script><script type="application/json" id="data-bag-config">{"csrfToken": "HEgRtNYBT4mXo2GjeqVlclYL94uKQjIQJcGn8mxli5bvL6cBzVXkMCxM7otzGQuk", "supportEmail": "support@codility.com", "upgradeEmail": "upgrades@codility.com", "collaborateUrl": "https://app.codility.com/services/codelive/collaborate/", "staticUrl": "/static/", "isRecruiter": false, "cacheId": "a56e3406b9b56cfe0d170cbb7660a2da4dee8f51", "logRocketId": "codility/frontend-jzrmw", "pendo": {"projectApiKey": "c6ae7399-061a-4c96-677e-4dca765e00f5", "includeUserPII": true, "site": "US"}}</script>
<script type="application/json" id="data-bag-external-urls">{"analytics_survey": "https://www.surveymonkey.com/r/V9WY87X", "automated_reports": "https://automated-reports.data.codility.net/", "blog": "https://www.codility.com/blog/", "codelive_product_tour": "https://www.codility.com/product-tour/codelive/", "product_tour": "https://www.codility.com/product-tour/", "cookie_policy": "https://www.codility.com/cookie-policy/", "data_privacy_notice": "https://www.codility.com/data-privacy-notice/", "data_processing_agreement": "https://www.codility.com/data-processing-agreement/", "demo": "https://www.codility.com/request-a-demo/", "dmca_policy": "https://www.codility.com/dmca-policy/", "facebook_profile": "https://www.facebook.com/Codility/", "fair_use_policy": "https://www.codility.com/fair-use-policy/", "github_profile": "https://github.com/Codility/", "help_center": "https://support.codility.com/", "help_center_analytics": "https://support.codility.com/hc/en-us/articles/360055451253-Analytics-Dashboard", "help_center_anti_cheating_methods": "https://support.codility.com/hc/en-us/articles/360043319434-Anti-Cheating-Methods", "help_center_cancellation_and_refund": "https://support.codility.com/hc/en-us/articles/360043824333-Cancellation-and-Refund-policies", "help_center_codelive_interview": " https://support.codility.com/hc/en-us/articles/360043828053-How-to-Use-CodeLive", "help_center_codelive_room_types": "https://support.codility.com/hc/en-us/articles/360043318154-Different-Formats-of-CodeLive-Rooms", "help_center_custom_tasks": "https://support.codility.com/hc/en-us/articles/360043319994-Exclusive-Tasks", "help_center_fairness_rating": "https://support.codility.com/hc/en-us/articles/360051585814-What-does-Fairness-Rating-mean-", "help_center_greenhouse": "https://support.codility.com/hc/en-us/articles/360043824653-Integrating-with-Greenhouse", "help_center_icims": "https://support.codility.com/hc/en-us/articles/360043317754-Integrating-with-iCIMS", "help_center_jobvite": "https://support.codility.com/hc/en-us/articles/360043317794-Integrating-with-Jobvite", "help_center_lever": "https://support.codility.com/hc/en-us/articles/360043317954-Integrating-with-Lever-ATS", "help_center_recruitee": "https://support.codility.com/hc/en-us/articles/360043317974-Integrating-with-Recruitee", "help_center_reopening_sessions": "https://support.codility.com/hc/en-us/articles/360043826173-Reopening-Tests-for-Candidates", "help_center_similarity_check": "https://support.codility.com/hc/en-us/articles/360043825273-Similarity-check-and-what-to-do", "help_center_slack": "https://support.codility.com/hc/en-us/articles/360043824553-Integrating-with-Slack", "help_center_smartrecruiters": "https://support.codility.com/hc/en-us/articles/360043824613-Integrating-with-SmartRecruiters", "help_center_taleo": "https://support.codility.com/hc/en-us/articles/360043317994-Integrating-with-Oracle-s-Taleo", "help_center_teamtailor": "https://support.codility.com/hc/en-us/articles/360052599973-Integrating-with-Teamtailor-ATS", "help_center_training": "https://support.codility.com/hc/en-us/articles/360043318034-Using-Codility-for-Training", "help_center_training_videos": "https://support.codility.com/hc/en-us/sections/360008588994-Training-Videos", "help_center_weighted_scoring": "https://support.codility.com/hc/en-us/articles/360047471133-Weighted-Scoring", "help_center_supported_browsers_cui": "https://support.codility.com/hc/en-us/articles/360046335994-What-browsers-are-supported-", "help_center_supported_browsers_rui": "https://support.codility.com/hc/en-us/articles/360043823313-What-browsers-are-supported-", "help_center_workable": "https://support.codility.com/hc/en-us/articles/360043317874-Integrating-with-Workable", "help_center_linkedin_talenthub": "https://support.codility.com/hc/en-us/articles/4415522256919-Integrating-with-LinkedIn-Talent-Solutions", "help_center_anti_bias_workflow": "https://support.codility.com/hc/en-us/articles/360050024513-Anonymization-Anti-bias-features", "help_center_creating_a_great_screening_test": "https://support.codility.com/hc/en-us/articles/360043320374-Creating-a-Great-Screening-Test", "help_center_encourage_more_candidates_to_take_my_tests": "https://support.codility.com/hc/en-us/articles/360043823833-How-can-I-encourage-more-of-my-candidates-to-take-my-test-", "help_center_review_workflow": "https://support.codility.com/hc/en-us/articles/360055796114-Candidate-Review-Workflow", "help_center_review_workflow_multiple_reviewers": "https://support.codility.com/hc/en-us/articles/360055796114-Candidate-Review-Workflow#multiple_reviewers", "help_center_permission_levels": "https://support.codility.com/hc/en-us/articles/360043317574-Permission-Levels", "help_center_invite_expiration": "https://support.codility.com/hc/en-us/articles/4415859889175", "help_center_how_to_invite_candidate": "https://support.codility.com/hc/en-us/articles/360043826673-How-to-Invite-Candidates", "help_center_softgarden": "https://support.codility.com/hc/en-us/articles/360053997293-Integrating-with-softgarden", "help_center_freshteam": "https://support.codility.com/hc/en-us/articles/1500002443402-Integration-with-Freshteam", "help_center_naukri_rms": "https://support.codility.com/hc/en-us/articles/360061163174-Integrating-with-Naukri-RMS", "help_center_goodtime": "https://support.codility.com/hc/en-us/articles/4408493605015", "help_center_ashby": "https://support.codility.com/hc/en-us/articles/9990111645719-Integrating-with-Ashby", "help_center_manatal": "https://support.manatal.com/docs/codility", "help_center_pinpoint": "https://support.codility.com/hc/en-us/articles/6952353448087-Integrating-with-Pinpoint", "help_center_workday": "https://engage.codility.com/rs/024-OPP-333/images/Workday%20and%20Codility%20Integration%20Deployment%20Guide.pdf", "homepage": "https://www.codility.com", "jobs": "https://apply.workable.com/codility/", "linkedin_profile": "https://www.linkedin.com/company/codility", "new_pdf_report_only_on_staging": "https://jenson.herokuapp.com/pdf", "pricing": "https://www.codility.com/pricing/", "privacy_policy": "https://www.codility.com/privacy-policy/", "referral_greenhouse": "https://go.greenhouse.io/referral-codility.html", "referral_icims": "https://www3.icims.com/mktg/identify-and-hire-the-most-qualified-candidates/?type=partner&utm_campaign=701i0000001uqgv", "referral_jobvite": "http://web.jobvite.com/FY17_Website_Codility_Demo_LP.html", "referral_recruitee": "https://recruitee.com/demo/form?utm_medium=affiliate&utm_source=codility&utm_campaign=codility", "referral_smartrecruiter": "https://www.smartrecruiters.com/resources/get-a-demo/?utm_source=codility_promo", "releases": "https://support.codility.com/hc/en-us/categories/360003126813", "terms_of_service_for_companies": "https://www.codility.com/terms-of-service/", "twilio_network_check": "https://networktest.twilio.com", "twitter_profile": "https://twitter.com/Codility", "twitter_share_challenge": "https://twitter.com/intent/tweet", "linkedin_share_challenge": "https://www.linkedin.com/profile/add", "typeform_candidate_survey": "https://codility.typeform.com/to/:id", "typeform_candidate_survey_reports": "https://codility.typeform.com/report/:id", "typeform_codelive_recruiter_survey": "https://codility.typeform.com/to/:id", "typeform_codelive_candidate_survey": "https://codility.typeform.com/to/:id", "typeform_sponsored_challenge_diversity_survey": "https://codility.typeform.com/to/:id", "weighted_scoring_blog_page": "https://www.codility.com/blog/new-find-the-right-candidate-for-right-now-with-weighted-scoring/", "salesforce_search": "https://emea.salesforce.com/_ui/search/ui/UnifiedSearchResults", "identity_verification_learn_more_blog_post": "https://support.codility.com/hc/en-us/articles/360060045273-Identity-Verification", "youtube_profile": "https://www.youtube.com/user/codility", "homepage_customer_newsletter": "https://www.codility.com/customer-newsletter-sign-up/?utm_source=homepage&utm_medium=product&utm_campaign=customer-newsletter", "homepage_product_spotlight": "https://www.codility.com/knowledge-hub/product-spotlight-recordings/?utm_source=homepage&utm_medium=product&utm_campaign=product-spotlight", "homepage_virtual_learning": "https://www.codility.com/knowledge-hub/events-and-webinars/?utm_source=homepage&utm_medium=product&utm_campaign=events", "homepage_blog": "https://www.codility.com/blog/?utm_source=homepage&utm_medium=product&utm_campaign=blog", "login_step2_need_help": "https://support.codility.com/hc/en-us/articles/4403106904599", "host_coding_challenges": "https://www.codility.com/product-tour/coding-challenges/", "talent_hub_integrations": "https://www.linkedin.com/talent/account/v2/integrations", "greenhouse_codecheck_integrations": "https://app.greenhouse.io/integrations", "integrate_recruitee": "https://app.recruitee.com/#/settings/integrations?integrate=codility"}</script>

<!-- programmers_home analytics --><script type="application/json" id="data-bag-analytics">{"request_metrics": {"token": "k7wm2hr:e7qj7yj"}}</script>

<script nonce="" src="./binarygap_files/jquery-3.6.0.min.js.download"></script>
<script nonce="" src="./binarygap_files/jquery-migrate-3.4.0.min.js.download"></script>
<script nonce="" src="./binarygap_files/semantic.min.js.download"></script>
<script nonce="" src="./binarygap_files/jquery.jqModal.js.download"></script>


<script nonce="" src="./binarygap_files/cui-css-loader.js.download"></script><link href="./binarygap_files/c6c49be64853362959e2.cui.css" rel="stylesheet">
<script nonce="" src="./binarygap_files/cui-js-loader.js.download"></script><script src="./binarygap_files/427b5f9a7bfe620ad4f3.runtime.auto.js.js.download"></script><script src="./binarygap_files/a1141001fe499bb1e1ad.3513.js.download"></script><script src="./binarygap_files/d8ec2d55e8b96e6ee51f.polyfills.js.download"></script><script src="./binarygap_files/ccde795e19b356e7be5e.8929.js.download"></script><script src="./binarygap_files/936f2d52f452dd30f0da.analytics.js.download"></script><script src="./binarygap_files/b5c4d181083319ae53ea.8535.js.download"></script><script src="./binarygap_files/66e6e7fbc6acb9446ceb.cui.js.download"></script>

  
  <meta name="google-site-verification" content="9v164Z_rpdjfMPb9gqiXp6m3zBjJVhoZTwvA3Qj0eIc">
  

  



<script src="./binarygap_files/rm.js.download" async="" data-rm-token="k7wm2hr:e7qj7yj" data-rm-tags="us-cluster,cui"></script><script src="./binarygap_files/logger-1.min.js.download" async=""></script><script src="./binarygap_files/pendo.js.download" id="pendo" type="text/javascript" async=""></script><style data-styled="active" data-styled-version="5.3.5"></style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .accessibilityHelpWidget {
	padding: 10px;
	vertical-align: middle;
	overflow: scroll;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-aria-container {
	position: absolute; /* try to hide from window but not from screen readers */
	left:-999em;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .selection-anchor {
	background-color: #007ACC;
	width: 2px !important;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .bracket-match {
	box-sizing: border-box;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .monaco-editor-overlaymessage {
	padding-bottom: 8px;
	z-index: 10000;
}

.monaco-editor .monaco-editor-overlaymessage.below {
	padding-bottom: 0;
	padding-top: 8px;
	z-index: 10000;
}

@keyframes fadeIn {
	from { opacity: 0; }
	to { opacity: 1; }
}
.monaco-editor .monaco-editor-overlaymessage.fadeIn {
	animation: fadeIn 150ms ease-out;
}

@keyframes fadeOut {
	from { opacity: 1; }
	to { opacity: 0; }
}
.monaco-editor .monaco-editor-overlaymessage.fadeOut {
	animation: fadeOut 100ms ease-out;
}

.monaco-editor .monaco-editor-overlaymessage .message {
	padding: 1px 4px;
}

.monaco-editor .monaco-editor-overlaymessage .anchor {
	width: 0 !important;
	height: 0 !important;
	border-color: transparent;
	border-style: solid;
	z-index: 1000;
	border-width: 8px;
	position: absolute;
}

.monaco-editor .monaco-editor-overlaymessage:not(.below) .anchor.top,
.monaco-editor .monaco-editor-overlaymessage.below .anchor.below {
	display: none;
}

.monaco-editor .monaco-editor-overlaymessage.below .anchor.top {
	display: inherit;
	top: -8px;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .contentWidgets .codicon-light-bulb,
.monaco-editor .contentWidgets .codicon-lightbulb-autofix {
	display: flex;
	align-items: center;
	justify-content: center;
}

.monaco-editor .contentWidgets .codicon-light-bulb:hover,
.monaco-editor .contentWidgets .codicon-lightbulb-autofix:hover {
	cursor: pointer;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .codelens-decoration {
	overflow: hidden;
	display: inline-block;
	text-overflow: ellipsis;
	white-space: nowrap;
}

.monaco-editor .codelens-decoration > span,
.monaco-editor .codelens-decoration > a {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
	white-space: nowrap;
	vertical-align: sub;
}

.monaco-editor .codelens-decoration > a {
	text-decoration: none;
}

.monaco-editor .codelens-decoration > a:hover {
	cursor: pointer;
}

.monaco-editor .codelens-decoration .codicon {
	vertical-align: middle;
	color: currentColor !important;
}

.monaco-editor .codelens-decoration > a:hover .codicon::before {
	cursor: pointer;
}

@keyframes fadein {
	0% { opacity: 0; visibility: visible;}
	100% { opacity: 1; }
}

.monaco-editor .codelens-decoration.fadein {
	animation: fadein 0.1s linear;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .goto-definition-link {
	text-decoration: underline;
	cursor: pointer;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-action-bar {
	white-space: nowrap;
	height: 100%;
}

.monaco-action-bar .actions-container {
	display: flex;
	margin: 0 auto;
	padding: 0;
	height: 100%;
	width: 100%;
	align-items: center;
}

.monaco-action-bar.vertical .actions-container {
	display: inline-block;
}

.monaco-action-bar .action-item {
	display: block;
	align-items: center;
	justify-content: center;
	cursor: pointer;
	position: relative;  /* DO NOT REMOVE - this is the key to preventing the ghosting icon bug in Chrome 42 */
}

.monaco-action-bar .action-item.disabled {
	cursor: default;
}

.monaco-action-bar .action-item .icon,
.monaco-action-bar .action-item .codicon {
	display: block;
}

.monaco-action-bar .action-item .codicon {
	display: flex;
	align-items: center;
	width: 16px;
	height: 16px;
}

.monaco-action-bar .action-label {
	font-size: 11px;
	padding: 3px;
	border-radius: 5px;
}

.monaco-action-bar .action-item.disabled .action-label,
.monaco-action-bar .action-item.disabled .action-label::before,
.monaco-action-bar .action-item.disabled .action-label:hover {
	opacity: 0.4;
}

/* Vertical actions */

.monaco-action-bar.vertical {
	text-align: left;
}

.monaco-action-bar.vertical .action-item {
	display: block;
}

.monaco-action-bar.vertical .action-label.separator {
	display: block;
	border-bottom: 1px solid #bbb;
	padding-top: 1px;
	margin-left: .8em;
	margin-right: .8em;
}

.monaco-action-bar .action-item .action-label.separator {
	width: 1px;
	height: 16px;
	margin: 5px 4px !important;
	cursor: default;
	min-width: 1px;
	padding: 0;
	background-color: #bbb;
}

.secondary-actions .monaco-action-bar .action-label {
	margin-left: 6px;
}

/* Action Items */
.monaco-action-bar .action-item.select-container {
	overflow: hidden; /* somehow the dropdown overflows its container, we prevent it here to not push */
	flex: 1;
	max-width: 170px;
	min-width: 60px;
	display: flex;
	align-items: center;
	justify-content: center;
	margin-right: 10px;
}

.monaco-action-bar .action-item.action-dropdown-item {
	display: flex;
}

.monaco-action-bar .action-item.action-dropdown-item > .action-label {
	margin-right: 1px;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .peekview-widget .head {
	box-sizing: border-box;
	display: flex;
}

.monaco-editor .peekview-widget .head .peekview-title {
	display: flex;
	align-items: center;
	font-size: 13px;
	margin-left: 20px;
	min-width: 0;
}

.monaco-editor .peekview-widget .head .peekview-title.clickable {
	cursor: pointer;
}

.monaco-editor .peekview-widget .head .peekview-title .dirname:not(:empty) {
	font-size: 0.9em;
	margin-left: 0.5em;
}

.monaco-editor .peekview-widget .head .peekview-title .meta {
	white-space: nowrap;
}

.monaco-editor .peekview-widget .head .peekview-title .dirname {
	white-space: nowrap;
}

.monaco-editor .peekview-widget .head .peekview-title .filename {
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
}

.monaco-editor .peekview-widget .head .peekview-title .meta:not(:empty)::before {
	content: '-';
	padding: 0 0.3em;
}

.monaco-editor .peekview-widget .head .peekview-actions {
	flex: 1;
	text-align: right;
	padding-right: 2px;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar {
	display: inline-block;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar,
.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar > .actions-container {
	height: 100%;
}

.monaco-editor .peekview-widget > .body {
	border-top: 1px solid;
	position: relative;
}

.monaco-editor .peekview-widget .head .peekview-title .codicon {
	margin-right: 4px;
}

.monaco-editor .peekview-widget .monaco-list .monaco-list-row.focused .codicon {
	color: inherit !important;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* -------------------- IE10 remove auto clear button -------------------- */

::-ms-clear {
	display: none;
}

/* All widgets */
/* I am not a big fan of this rule */
.monaco-editor .editor-widget input {
	color: inherit;
}

/* -------------------- Editor -------------------- */

.monaco-editor {
	position: relative;
	overflow: visible;
	-webkit-text-size-adjust: 100%;
}

/* -------------------- Misc -------------------- */

.monaco-editor .overflow-guard {
	position: relative;
	overflow: hidden;
}

.monaco-editor .view-overlays {
	position: absolute;
	top: 0;
}

/*
.monaco-editor .auto-closed-character {
	opacity: 0.3;
}
*/
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .inputarea {
	min-width: 0;
	min-height: 0;
	margin: 0;
	padding: 0;
	position: absolute;
	outline: none !important;
	resize: none;
	border: none;
	overflow: hidden;
	color: transparent;
	background-color: transparent;
}
/*.monaco-editor .inputarea {
	position: fixed !important;
	width: 800px !important;
	height: 500px !important;
	top: initial !important;
	left: initial !important;
	bottom: 0 !important;
	right: 0 !important;
	color: black !important;
	background: white !important;
	line-height: 15px !important;
	font-size: 14px !important;
}*/
.monaco-editor .inputarea.ime-input {
	z-index: 10;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .margin-view-overlays .line-numbers {
	font-variant-numeric: tabular-nums;
	position: absolute;
	text-align: right;
	display: inline-block;
	vertical-align: middle;
	box-sizing: border-box;
	cursor: default;
	height: 100%;
}

.monaco-editor .relative-current-line-number {
	text-align: left;
	display: inline-block;
	width: 100%;
}

.monaco-editor .margin-view-overlays .line-numbers.lh-odd {
	margin-top: 1px;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-mouse-cursor-text {
	cursor: text;
}

/* The following selector looks a bit funny, but that is needed to cover all the workbench and the editor!! */
.vs-dark .mac .monaco-mouse-cursor-text, .hc-black .mac .monaco-mouse-cursor-text,
.vs-dark.mac .monaco-mouse-cursor-text, .hc-black.mac .monaco-mouse-cursor-text {
	cursor: -webkit-image-set(url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAQAAAC1+jfqAAAAL0lEQVQoz2NgCD3x//9/BhBYBWdhgFVAiVW4JBFKGIa4AqD0//9D3pt4I4tAdAMAHTQ/j5Zom30AAAAASUVORK5CYII=) 1x, url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J/AAAAz0lEQVRIx2NgYGBY/R8I/vx5eelX3n82IJ9FxGf6tksvf/8FiTMQAcAGQMDvSwu09abffY8QYSAScNk45G198eX//yev73/4///701eh//kZSARckrNBRvz//+8+6ZohwCzjGNjdgQxkAg7B9WADeBjIBqtJCbhRA0YNoIkBSNmaPEMoNmA0FkYNoFKhapJ6FGyAH3nauaSmPfwI0v/3OukVi0CIZ+F25KrtYcx/CTIy0e+rC7R1Z4KMICVTQQ14feVXIbR695u14+Ir4gwAAD49E54wc1kWAAAAAElFTkSuQmCC) 2x) 5 8, text;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .view-overlays .current-line {
	display: block;
	position: absolute;
	left: 0;
	top: 0;
	box-sizing: border-box;
}

.monaco-editor .margin-view-overlays .current-line {
	display: block;
	position: absolute;
	left: 0;
	top: 0;
	box-sizing: border-box;
}

.monaco-editor .margin-view-overlays .current-line.current-line-margin.current-line-margin-both {
	border-right: 0;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cdr = core decorations rendering (div)
*/
.monaco-editor .lines-content .cdr {
	position: absolute;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Arrows */
.monaco-scrollable-element > .scrollbar > .scra {
	cursor: pointer;
	font-size: 11px !important;
}

.monaco-scrollable-element > .visible {
	opacity: 1;

	/* Background rule added for IE9 - to allow clicks on dom node */
	background:rgba(0,0,0,0);

	transition: opacity 100ms linear;
}
.monaco-scrollable-element > .invisible {
	opacity: 0;
	pointer-events: none;
}
.monaco-scrollable-element > .invisible.fade {
	transition: opacity 800ms linear;
}

/* Scrollable Content Inset Shadow */
.monaco-scrollable-element > .shadow {
	position: absolute;
	display: none;
}
.monaco-scrollable-element > .shadow.top {
	display: block;
	top: 0;
	left: 3px;
	height: 3px;
	width: 100%;
	box-shadow: #DDD 0 6px 6px -6px inset;
}
.monaco-scrollable-element > .shadow.left {
	display: block;
	top: 3px;
	left: 0;
	height: 100%;
	width: 3px;
	box-shadow: #DDD 6px 0 6px -6px inset;
}
.monaco-scrollable-element > .shadow.top-left-corner {
	display: block;
	top: 0;
	left: 0;
	height: 3px;
	width: 3px;
}
.monaco-scrollable-element > .shadow.top.left {
	box-shadow: #DDD 6px 6px 6px -6px inset;
}

/* ---------- Default Style ---------- */

.vs .monaco-scrollable-element > .scrollbar > .slider {
	background: rgba(100, 100, 100, .4);
}
.vs-dark .monaco-scrollable-element > .scrollbar > .slider {
	background: rgba(121, 121, 121, .4);
}
.hc-black .monaco-scrollable-element > .scrollbar > .slider {
	background: rgba(111, 195, 223, .6);
}

.monaco-scrollable-element > .scrollbar > .slider:hover {
	background: rgba(100, 100, 100, .7);
}
.hc-black .monaco-scrollable-element > .scrollbar > .slider:hover {
	background: rgba(111, 195, 223, .8);
}

.monaco-scrollable-element > .scrollbar > .slider.active {
	background: rgba(0, 0, 0, .6);
}
.vs-dark .monaco-scrollable-element > .scrollbar > .slider.active {
	background: rgba(191, 191, 191, .4);
}
.hc-black .monaco-scrollable-element > .scrollbar > .slider.active {
	background: rgba(111, 195, 223, 1);
}

.vs-dark .monaco-scrollable-element .shadow.top {
	box-shadow: none;
}

.vs-dark .monaco-scrollable-element .shadow.left {
	box-shadow: #000 6px 0 6px -6px inset;
}

.vs-dark .monaco-scrollable-element .shadow.top.left {
	box-shadow: #000 6px 6px 6px -6px inset;
}

.hc-black .monaco-scrollable-element .shadow.top {
	box-shadow: none;
}

.hc-black .monaco-scrollable-element .shadow.left {
	box-shadow: none;
}

.hc-black .monaco-scrollable-element .shadow.top.left {
	box-shadow: none;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .glyph-margin {
	position: absolute;
	top: 0;
}

/*
	Keeping name short for faster parsing.
	cgmr = core glyph margin rendering (div)
*/
.monaco-editor .margin-view-overlays .cgmr {
	position: absolute;
	display: flex;
	align-items: center;
	justify-content: center;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .lines-content .core-guide {
	position: absolute;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Uncomment to see lines flashing when they're painted */
/*.monaco-editor .view-lines > .view-line {
	background-color: none;
	animation-name: flash-background;
	animation-duration: 800ms;
}
@keyframes flash-background {
	0%   { background-color: lightgreen; }
	100% { background-color: none }
}*/

.monaco-editor.no-user-select .lines-content,
.monaco-editor.no-user-select .view-line,
.monaco-editor.no-user-select .view-lines {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-editor .view-lines {
	white-space: nowrap;
}

.monaco-editor .view-line {
	position: absolute;
	width: 100%;
}

.monaco-editor .mtkz {
	display: inline-block;
}

/* TODO@tokenization bootstrap fix */
/*.monaco-editor .view-line > span > span {
	float: none;
	min-height: inherit;
	margin-left: inherit;
}*/
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .lines-decorations {
	position: absolute;
	top: 0;
	background: white;
}

/*
	Keeping name short for faster parsing.
	cldr = core lines decorations rendering (div)
*/
.monaco-editor .margin-view-overlays .cldr {
	position: absolute;
	height: 100%;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cmdr = core margin decorations rendering (div)
*/
.monaco-editor .margin-view-overlays .cmdr {
	position: absolute;
	left: 0;
	width: 100%;
	height: 100%;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* START cover the case that slider is visible on mouseover */
.monaco-editor .minimap.slider-mouseover .minimap-slider {
	opacity: 0;
	transition: opacity 100ms linear;
}
.monaco-editor .minimap.slider-mouseover:hover .minimap-slider {
	opacity: 1;
}
.monaco-editor .minimap.slider-mouseover .minimap-slider.active {
	opacity: 1;
}
/* END cover the case that slider is visible on mouseover */

.monaco-editor .minimap-shadow-hidden {
	position: absolute;
	width: 0;
}
.monaco-editor .minimap-shadow-visible {
	position: absolute;
	left: -6px;
	width: 6px;
}
.monaco-editor.no-minimap-shadow .minimap-shadow-visible {
	position: absolute;
	left: -1px;
	width: 1px;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .overlayWidgets {
	position: absolute;
	top: 0;
	left:0;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .view-ruler {
	position: absolute;
	top: 0;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .scroll-decoration {
	position: absolute;
	top: 0;
	left: 0;
	height: 6px;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cslr = core selections layer rendering (div)
*/
.monaco-editor .lines-content .cslr {
	position: absolute;
}

.monaco-editor			.top-left-radius		{ border-top-left-radius: 3px; }
.monaco-editor			.bottom-left-radius		{ border-bottom-left-radius: 3px; }
.monaco-editor			.top-right-radius		{ border-top-right-radius: 3px; }
.monaco-editor			.bottom-right-radius	{ border-bottom-right-radius: 3px; }

.monaco-editor.hc-black .top-left-radius		{ border-top-left-radius: 0; }
.monaco-editor.hc-black .bottom-left-radius		{ border-bottom-left-radius: 0; }
.monaco-editor.hc-black .top-right-radius		{ border-top-right-radius: 0; }
.monaco-editor.hc-black .bottom-right-radius	{ border-bottom-right-radius: 0; }
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .cursors-layer {
	position: absolute;
	top: 0;
}

.monaco-editor .cursors-layer > .cursor {
	position: absolute;
	overflow: hidden;
}

/* -- smooth-caret-animation -- */
.monaco-editor .cursors-layer.cursor-smooth-caret-animation > .cursor {
	transition: all 80ms;
}

/* -- block-outline-style -- */
.monaco-editor .cursors-layer.cursor-block-outline-style > .cursor {
	box-sizing: border-box;
	background: transparent !important;
	border-style: solid;
	border-width: 1px;
}

/* -- underline-style -- */
.monaco-editor .cursors-layer.cursor-underline-style > .cursor {
	border-bottom-width: 2px;
	border-bottom-style: solid;
	background: transparent !important;
	box-sizing: border-box;
}

/* -- underline-thin-style -- */
.monaco-editor .cursors-layer.cursor-underline-thin-style > .cursor {
	border-bottom-width: 1px;
	border-bottom-style: solid;
	background: transparent !important;
	box-sizing: border-box;
}

@keyframes monaco-cursor-smooth {
	0%,
	20% {
		opacity: 1;
	}
	60%,
	100% {
		opacity: 0;
	}
}

@keyframes monaco-cursor-phase {
	0%,
	20% {
		opacity: 1;
	}
	90%,
	100% {
		opacity: 0;
	}
}

@keyframes monaco-cursor-expand {
	0%,
	20% {
		transform: scaleY(1);
	}
	80%,
	100% {
		transform: scaleY(0);
	}
}

.cursor-smooth {
	animation: monaco-cursor-smooth 0.5s ease-in-out 0s 20 alternate;
}

.cursor-phase {
	animation: monaco-cursor-phase 0.5s ease-in-out 0s 20 alternate;
}

.cursor-expand > .cursor {
	animation: monaco-cursor-expand 0.5s ease-in-out 0s 20 alternate;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

:root {
	--sash-size: 4px;
}

.monaco-sash {
	position: absolute;
	z-index: 35;
	touch-action: none;
}

.monaco-sash.disabled {
	pointer-events: none;
}

.monaco-sash.mac.vertical {
	cursor: col-resize;
}

.monaco-sash.vertical.minimum {
	cursor: e-resize;
}

.monaco-sash.vertical.maximum {
	cursor: w-resize;
}

.monaco-sash.mac.horizontal {
	cursor: row-resize;
}

.monaco-sash.horizontal.minimum {
	cursor: s-resize;
}

.monaco-sash.horizontal.maximum {
	cursor: n-resize;
}

.monaco-sash.disabled {
	cursor: default !important;
	pointer-events: none !important;
}

.monaco-sash.vertical {
	cursor: ew-resize;
	top: 0;
	width: var(--sash-size);
	height: 100%;
}

.monaco-sash.horizontal {
	cursor: ns-resize;
	left: 0;
	width: 100%;
	height: var(--sash-size);
}

.monaco-sash:not(.disabled) > .orthogonal-drag-handle {
	content: " ";
	height: calc(var(--sash-size) * 2);
	width: calc(var(--sash-size) * 2);
	z-index: 100;
	display: block;
	cursor: all-scroll;
	position: absolute;
}

.monaco-sash.horizontal.orthogonal-edge-north:not(.disabled)
	> .orthogonal-drag-handle.start,
.monaco-sash.horizontal.orthogonal-edge-south:not(.disabled)
	> .orthogonal-drag-handle.end {
	cursor: nwse-resize;
}

.monaco-sash.horizontal.orthogonal-edge-north:not(.disabled)
	> .orthogonal-drag-handle.end,
.monaco-sash.horizontal.orthogonal-edge-south:not(.disabled)
	> .orthogonal-drag-handle.start {
	cursor: nesw-resize;
}

.monaco-sash.vertical > .orthogonal-drag-handle.start {
	left: calc(var(--sash-size) * -0.5);
	top: calc(var(--sash-size) * -1);
}
.monaco-sash.vertical > .orthogonal-drag-handle.end {
	left: calc(var(--sash-size) * -0.5);
	bottom: calc(var(--sash-size) * -1);
}
.monaco-sash.horizontal > .orthogonal-drag-handle.start {
	top: calc(var(--sash-size) * -0.5);
	left: calc(var(--sash-size) * -1);
}
.monaco-sash.horizontal > .orthogonal-drag-handle.end {
	top: calc(var(--sash-size) * -0.5);
	right: calc(var(--sash-size) * -1);
}

.monaco-sash:before {
	content: '';
	pointer-events: none;
	position: absolute;
	width: 100%;
	height: 100%;
	transition: background-color 0.1s ease-out;
	background: transparent;
}

.monaco-sash.vertical:before {
	width: var(--sash-hover-size);
	left: calc(50% - (var(--sash-hover-size) / 2));
}

.monaco-sash.horizontal:before {
	height: var(--sash-hover-size);
	top: calc(50% - (var(--sash-hover-size) / 2));
}

/** Debug **/

.monaco-sash.debug {
	background: cyan;
}

.monaco-sash.debug.disabled {
	background: rgba(0, 255, 255, 0.2);
}

.monaco-sash.debug:not(.disabled) > .orthogonal-drag-handle {
	background: red;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .zone-widget {
	position: absolute;
	z-index: 10;
}


.monaco-editor .zone-widget .zone-widget-container {
	border-top-style: solid;
	border-bottom-style: solid;
	border-top-width: 0;
	border-bottom-width: 0;
	position: relative;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-dropdown {
	height: 100%;
	padding: 0;
}

.monaco-dropdown > .dropdown-label {
	cursor: pointer;
	height: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
}

.monaco-dropdown > .dropdown-label > .action-label.disabled {
	cursor: default;
}

.monaco-dropdown-with-primary {
	display: flex !important;
	flex-direction: row;
	border-radius: 5px;
}

.monaco-dropdown-with-primary > .action-container > .action-label {
	margin-right: 0;
}

.monaco-dropdown-with-primary > .dropdown-action-container > .monaco-dropdown > .dropdown-label .codicon[class*='codicon-'] {
	font-size: 12px;
	padding-left: 0px;
	padding-right: 0px;
	line-height: 16px;
	margin-left: -3px;
}

.monaco-dropdown-with-primary > .dropdown-action-container > .monaco-dropdown > .dropdown-label > .action-label {
	display: block;
	background-size: 16px;
	background-position: center center;
	background-repeat: no-repeat;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-action-bar .action-item.menu-entry .action-label.icon {
	width: 16px;
	height: 16px;
	background-repeat: no-repeat;
	background-position: 50%;
	background-size: 16px;
}

.monaco-action-bar .action-item.menu-entry .action-label {
	background-image: var(--menu-entry-icon-light);
}

.vs-dark .monaco-action-bar .action-item.menu-entry .action-label,
.hc-black .monaco-action-bar .action-item.menu-entry .action-label {
	background-image: var(--menu-entry-icon-dark);
}


.monaco-dropdown-with-default {
	display: flex !important;
	flex-direction: row;
	border-radius: 5px;
}

.monaco-dropdown-with-default > .action-container > .action-label {
	margin-right: 0;
}

.monaco-dropdown-with-default > .action-container.menu-entry > .action-label.icon {
	width: 16px;
	height: 16px;
	background-repeat: no-repeat;
	background-position: 50%;
	background-size: 16px;
}

.monaco-dropdown-with-default > .action-container.menu-entry > .action-label {
	background-image: var(--menu-entry-icon-light);
}

.vs-dark .monaco-dropdown-with-default > .action-container.menu-entry > .action-label,
.hc-black .monaco-dropdown-with-default > .action-container.menu-entry > .action-label {
	background-image: var(--menu-entry-icon-dark);
}

.monaco-dropdown-with-default > .dropdown-action-container > .monaco-dropdown > .dropdown-label .codicon[class*='codicon-'] {
	font-size: 12px;
	padding-left: 0px;
	padding-right: 0px;
	line-height: 16px;
	margin-left: -3px;
}

.monaco-dropdown-with-default > .dropdown-action-container > .monaco-dropdown > .dropdown-label > .action-label {
	display: block;
	background-size: 16px;
	background-position: center center;
	background-repeat: no-repeat;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-list {
	position: relative;
	height: 100%;
	width: 100%;
	white-space: nowrap;
}

.monaco-list.mouse-support {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-list > .monaco-scrollable-element {
	height: 100%;
}

.monaco-list-rows {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-list.horizontal-scrolling .monaco-list-rows {
	width: auto;
	min-width: 100%;
}

.monaco-list-row {
	position: absolute;
	box-sizing: border-box;
	overflow: hidden;
	width: 100%;
}

.monaco-list.mouse-support .monaco-list-row {
	cursor: pointer;
	touch-action: none;
}

/* for OS X ballistic scrolling */
.monaco-list-row.scrolling {
	display: none !important;
}

/* Focus */
.monaco-list.element-focused,
.monaco-list.selection-single,
.monaco-list.selection-multiple {
	outline: 0 !important;
}

/* Dnd */
.monaco-drag-image {
	display: inline-block;
	padding: 1px 7px;
	border-radius: 10px;
	font-size: 12px;
	position: absolute;
	z-index: 1000;
}

/* Type filter */

.monaco-list-type-filter {
	display: flex;
	align-items: center;
	position: absolute;
	border-radius: 2px;
	padding: 0px 3px;
	max-width: calc(100% - 10px);
	text-overflow: ellipsis;
	overflow: hidden;
	text-align: right;
	box-sizing: border-box;
	cursor: all-scroll;
	font-size: 13px;
	line-height: 18px;
	height: 20px;
	z-index: 1;
	top: 4px;
}

.monaco-list-type-filter.dragging {
	transition: top 0.2s, left 0.2s;
}

.monaco-list-type-filter.ne {
	right: 4px;
}

.monaco-list-type-filter.nw {
	left: 4px;
}

.monaco-list-type-filter > .controls {
	display: flex;
	align-items: center;
	box-sizing: border-box;
	transition: width 0.2s;
	width: 0;
}

.monaco-list-type-filter.dragging > .controls,
.monaco-list-type-filter:hover > .controls {
	width: 36px;
}

.monaco-list-type-filter > .controls > * {
	border: none;
	box-sizing: border-box;
	-webkit-appearance: none;
	-moz-appearance: none;
	background: none;
	width: 16px;
	height: 16px;
	flex-shrink: 0;
	margin: 0;
	padding: 0;
	display: flex;
	align-items: center;
	justify-content: center;
	cursor: pointer;
}

.monaco-list-type-filter > .controls > .filter {
	margin-left: 4px;
}

.monaco-list-type-filter-message {
	position: absolute;
	box-sizing: border-box;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	padding: 40px 1em 1em 1em;
	text-align: center;
	white-space: normal;
	opacity: 0.7;
	pointer-events: none;
}

.monaco-list-type-filter-message:empty {
	display: none;
}

/* Electron */

.monaco-list-type-filter {
	cursor: grab;
}

.monaco-list-type-filter.dragging {
	cursor: grabbing;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-split-view2 {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-split-view2 > .sash-container {
	position: absolute;
	width: 100%;
	height: 100%;
	pointer-events: none;
}

.monaco-split-view2 > .sash-container > .monaco-sash {
	pointer-events: initial;
}

.monaco-split-view2 > .monaco-scrollable-element {
	width: 100%;
	height: 100%;
}

.monaco-split-view2 > .monaco-scrollable-element > .split-view-container {
	width: 100%;
	height: 100%;
	white-space: nowrap;
	position: relative;
}

.monaco-split-view2 > .monaco-scrollable-element > .split-view-container > .split-view-view {
	white-space: initial;
	position: absolute;
}

.monaco-split-view2 > .monaco-scrollable-element > .split-view-container > .split-view-view:not(.visible) {
	display: none;
}

.monaco-split-view2.vertical > .monaco-scrollable-element > .split-view-container > .split-view-view {
	width: 100%;
}

.monaco-split-view2.horizontal > .monaco-scrollable-element > .split-view-container > .split-view-view {
	height: 100%;
}

.monaco-split-view2.separator-border > .monaco-scrollable-element > .split-view-container > .split-view-view:not(:first-child)::before {
	content: ' ';
	position: absolute;
	top: 0;
	left: 0;
	z-index: 5;
	pointer-events: none;
	background-color: var(--separator-border);
}

.monaco-split-view2.separator-border.horizontal > .monaco-scrollable-element > .split-view-container > .split-view-view:not(:first-child)::before {
	height: 100%;
	width: 1px;
}

.monaco-split-view2.separator-border.vertical > .monaco-scrollable-element > .split-view-container > .split-view-view:not(:first-child)::before {
	height: 1px;
	width: 100%;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-table {
	display: flex;
	flex-direction: column;
	position: relative;
	height: 100%;
	width: 100%;
	white-space: nowrap;
}

.monaco-table > .monaco-split-view2 {
	border-bottom: 1px solid transparent;
}

.monaco-table > .monaco-list {
	flex: 1;
}

.monaco-table-tr {
	display: flex;
	height: 100%;
}

.monaco-table-th {
	width: 100%;
	height: 100%;
	font-weight: bold;
	overflow: hidden;
	text-overflow: ellipsis;
}

.monaco-table-th,
.monaco-table-td {
	box-sizing: border-box;
	flex-shrink: 0;
	overflow: hidden;
	white-space: nowrap;
	text-overflow: ellipsis;
}

.monaco-table > .monaco-split-view2 .monaco-sash.vertical::before {
	content: "";
	position: absolute;
	left: calc(var(--sash-size) / 2);
	width: 0;
	border-left: 1px solid transparent;
}

.monaco-table > .monaco-split-view2,
.monaco-table > .monaco-split-view2 .monaco-sash.vertical::before {
	transition: border-color 0.2s ease-out;
}
/*
.monaco-table:hover > .monaco-split-view2,
.monaco-table:hover > .monaco-split-view2 .monaco-sash.vertical::before {
	border-color: rgba(204, 204, 204, 0.2);
} */
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-tl-row {
	display: flex;
	height: 100%;
	align-items: center;
	position: relative;
}

.monaco-tl-indent {
	height: 100%;
	position: absolute;
	top: 0;
	left: 16px;
	pointer-events: none;
}

.hide-arrows .monaco-tl-indent {
	left: 12px;
}

.monaco-tl-indent > .indent-guide {
	display: inline-block;
	box-sizing: border-box;
	height: 100%;
	border-left: 1px solid transparent;
}

.monaco-tl-indent > .indent-guide {
	transition: border-color 0.1s linear;
}

.monaco-tl-twistie,
.monaco-tl-contents {
	height: 100%;
}

.monaco-tl-twistie {
	font-size: 10px;
	text-align: right;
	padding-right: 6px;
	flex-shrink: 0;
	width: 16px;
	display: flex !important;
	align-items: center;
	justify-content: center;
	transform: translateX(3px);
}

.monaco-tl-contents {
	flex: 1;
	overflow: hidden;
}

.monaco-tl-twistie::before {
	border-radius: 20px;
}

.monaco-tl-twistie.collapsed::before {
	transform: rotate(-90deg);
}

.monaco-tl-twistie.codicon-tree-item-loading::before {
	/* Use steps to throttle FPS to reduce CPU usage */
	animation: codicon-spin 1.25s steps(30) infinite;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* -- zone widget */
.monaco-editor .zone-widget .zone-widget-container.reference-zone-widget {
	border-top-width: 1px;
	border-bottom-width: 1px;
}

.monaco-editor .reference-zone-widget .inline {
	display: inline-block;
	vertical-align: top;
}

.monaco-editor .reference-zone-widget .messages {
	height: 100%;
	width: 100%;
	text-align: center;
	padding: 3em 0;
}

.monaco-editor .reference-zone-widget .ref-tree {
	line-height: 23px;
}

.monaco-editor .reference-zone-widget .ref-tree .reference {
	text-overflow: ellipsis;
	overflow: hidden;
}

.monaco-editor .reference-zone-widget .ref-tree .reference-file {
	display: inline-flex;
	width: 100%;
	height: 100%;
}

.monaco-editor .reference-zone-widget .ref-tree .monaco-list:focus .selected .reference-file {
	color: inherit !important;
}

.monaco-editor .reference-zone-widget .ref-tree .reference-file .count {
	margin-right: 12px;
	margin-left: auto;
}

/* High Contrast Theming */

.monaco-editor.hc-black .reference-zone-widget .ref-tree .reference-file {
	font-weight: bold;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-count-badge {
	padding: 3px 6px;
	border-radius: 11px;
	font-size: 11px;
	min-width: 18px;
	min-height: 18px;
	line-height: 11px;
	font-weight: normal;
	text-align: center;
	display: inline-block;
	box-sizing: border-box;
}

.monaco-count-badge.long {
	padding: 2px 3px;
	border-radius: 2px;
	min-height: auto;
	line-height: normal;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* ---------- Icon label ---------- */

.monaco-icon-label {
	display: flex; /* required for icons support :before rule */
	overflow: hidden;
	text-overflow: ellipsis;
}

.monaco-icon-label::before {

	/* svg icons rendered as background image */
	background-size: 16px;
	background-position: left center;
	background-repeat: no-repeat;
	padding-right: 6px;
	width: 16px;
	height: 22px;
	line-height: inherit !important;
	display: inline-block;

	/* fonts icons */
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	vertical-align: top;

	flex-shrink: 0; /* fix for https://github.com/microsoft/vscode/issues/13787 */
}

.monaco-icon-label > .monaco-icon-label-container {
	min-width: 0;
	overflow: hidden;
	text-overflow: ellipsis;
	flex: 1;
}

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-name-container > .label-name {
	color: inherit;
	white-space: pre; /* enable to show labels that include multiple whitespaces */
}

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-name-container > .label-name > .label-separator {
	margin: 0 2px;
	opacity: 0.5;
}

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-description-container > .label-description {
	opacity: .7;
	margin-left: 0.5em;
	font-size: 0.9em;
	white-space: pre; /* enable to show labels that include multiple whitespaces */
}

.monaco-icon-label.nowrap > .monaco-icon-label-container > .monaco-icon-description-container > .label-description{
	white-space: nowrap
}

.vs .monaco-icon-label > .monaco-icon-label-container > .monaco-icon-description-container > .label-description {
	opacity: .95;
}

.monaco-icon-label.italic > .monaco-icon-label-container > .monaco-icon-name-container > .label-name,
.monaco-icon-label.italic > .monaco-icon-label-container > .monaco-icon-description-container > .label-description {
	font-style: italic;
}

.monaco-icon-label.deprecated {
	text-decoration: line-through;
	opacity: 0.66;
}

/* make sure apply italic font style to decorations as well */
.monaco-icon-label.italic::after {
	font-style: italic;
}

.monaco-icon-label.strikethrough > .monaco-icon-label-container > .monaco-icon-name-container > .label-name,
.monaco-icon-label.strikethrough > .monaco-icon-label-container > .monaco-icon-description-container > .label-description {
	text-decoration: line-through;
}

.monaco-icon-label::after {
	opacity: 0.75;
	font-size: 90%;
	font-weight: 600;
	margin: auto 16px 0 5px; /* https://github.com/microsoft/vscode/issues/113223 */
	text-align: center;
}

/* make sure selection color wins when a label is being selected */
.monaco-list:focus .selected .monaco-icon-label, /* list */
.monaco-list:focus .selected .monaco-icon-label::after
{
	color: inherit !important;
}

.monaco-list-row.focused.selected .label-description,
.monaco-list-row.selected .label-description {
	opacity: .8;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-hover {
	cursor: default;
	position: absolute;
	overflow: hidden;
	z-index: 50;
	user-select: text;
	-webkit-user-select: text;
	-ms-user-select: text;
	box-sizing: initial;
	animation: fadein 100ms linear;
	line-height: 1.5em;
}

.monaco-hover.hidden {
	display: none;
}

.monaco-hover .hover-contents:not(.html-hover-contents) {
	padding: 4px 8px;
}

.monaco-hover .markdown-hover > .hover-contents:not(.code-hover-contents) {
	max-width: 500px;
	word-wrap: break-word;
}

.monaco-hover .markdown-hover > .hover-contents:not(.code-hover-contents) hr {
	min-width: 100%;
}

.monaco-hover p,
.monaco-hover .code,
.monaco-hover ul {
	margin: 8px 0;
}

.monaco-hover code {
	font-family: var(--monaco-monospace-font);
}

.monaco-hover hr {
	box-sizing: border-box;
	border-left: 0px;
	border-right: 0px;
	margin-top: 4px;
	margin-bottom: -4px;
	margin-left: -8px;
	margin-right: -8px;
	height: 1px;
}

.monaco-hover p:first-child,
.monaco-hover .code:first-child,
.monaco-hover ul:first-child {
	margin-top: 0;
}

.monaco-hover p:last-child,
.monaco-hover .code:last-child,
.monaco-hover ul:last-child {
	margin-bottom: 0;
}

/* MarkupContent Layout */
.monaco-hover ul {
	padding-left: 20px;
}
.monaco-hover ol {
	padding-left: 20px;
}

.monaco-hover li > p {
	margin-bottom: 0;
}

.monaco-hover li > ul {
	margin-top: 0;
}

.monaco-hover code {
	border-radius: 3px;
	padding: 0 0.4em;
}

.monaco-hover .monaco-tokenized-source {
	white-space: pre-wrap;
}

.monaco-hover .hover-row.status-bar {
	font-size: 12px;
	line-height: 22px;
}

.monaco-hover .hover-row.status-bar .actions {
	display: flex;
	padding: 0px 8px;
}

.monaco-hover .hover-row.status-bar .actions .action-container {
	margin-right: 16px;
	cursor: pointer;
}

.monaco-hover .hover-row.status-bar .actions .action-container .action .icon {
	padding-right: 4px;
}

.monaco-hover .markdown-hover .hover-contents .codicon {
	color: inherit;
	font-size: inherit;
	vertical-align: middle;
}

.monaco-hover .hover-contents a.code-link:hover,
.monaco-hover .hover-contents a.code-link {
	color: inherit;
}

.monaco-hover .hover-contents a.code-link:before {
	content: '(';
}

.monaco-hover .hover-contents a.code-link:after {
	content: ')';
}

.monaco-hover .hover-contents a.code-link > span {
	text-decoration: underline;
	/** Hack to force underline to show **/
	border-bottom: 1px solid transparent;
	text-underline-position: under;
}

/** Spans in markdown hovers need a margin-bottom to avoid looking cramped: https://github.com/microsoft/vscode/issues/101496 **/
.monaco-hover .markdown-hover .hover-contents:not(.code-hover-contents):not(.html-hover-contents) span {
	margin-bottom: 4px;
	display: inline-block;
}

.monaco-hover-content .action-container a {
	-webkit-user-select: none;
	user-select: none;
}

.monaco-hover-content .action-container.disabled {
	pointer-events: none;
	opacity: 0.4;
	cursor: default;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.colorpicker-widget {
	height: 190px;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-editor .colorpicker-hover:focus {
	outline: none;
}


/* Header */

.colorpicker-header {
	display: flex;
	height: 24px;
	position: relative;
	background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp8Z5+AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTZEaa/1AAAAHUlEQVQYV2PYvXu3JAi7uLiAMaYAjAGTQBPYLQkAa/0Zef3qRswAAAAASUVORK5CYII=);
	background-size: 9px 9px;
	image-rendering: pixelated;
}

.colorpicker-header .picked-color {
	width: 216px;
	text-align: center;
	line-height: 24px;
	cursor: pointer;
	color: white;
	flex: 1;
	text-align: center;
}

.colorpicker-header .picked-color.light {
	color: black;
}

.colorpicker-header .original-color {
	width: 74px;
	z-index: inherit;
	cursor: pointer;
}


/* Body */

.colorpicker-body {
	display: flex;
	padding: 8px;
	position: relative;
}

.colorpicker-body .saturation-wrap {
	overflow: hidden;
	height: 150px;
	position: relative;
	min-width: 220px;
	flex: 1;
}

.colorpicker-body .saturation-box {
	height: 150px;
	position: absolute;
}

.colorpicker-body .saturation-selection {
	width: 9px;
	height: 9px;
	margin: -5px 0 0 -5px;
	border: 1px solid rgb(255, 255, 255);
	border-radius: 100%;
	box-shadow: 0px 0px 2px rgba(0, 0, 0, 0.8);
	position: absolute;
}

.colorpicker-body .strip {
	width: 25px;
	height: 150px;
}

.colorpicker-body .hue-strip {
	position: relative;
	margin-left: 8px;
	cursor: grab;
	background: linear-gradient(to bottom, #ff0000 0%, #ffff00 17%, #00ff00 33%, #00ffff 50%, #0000ff 67%, #ff00ff 83%, #ff0000 100%);
}

.colorpicker-body .opacity-strip {
	position: relative;
	margin-left: 8px;
	cursor: grab;
	background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp8Z5+AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTZEaa/1AAAAHUlEQVQYV2PYvXu3JAi7uLiAMaYAjAGTQBPYLQkAa/0Zef3qRswAAAAASUVORK5CYII=);
	background-size: 9px 9px;
	image-rendering: pixelated;
}

.colorpicker-body .strip.grabbing {
	cursor: grabbing;
}

.colorpicker-body .slider {
	position: absolute;
	top: 0;
	left: -2px;
	width: calc(100% + 4px);
	height: 4px;
	box-sizing: border-box;
	border: 1px solid rgba(255, 255, 255, 0.71);
	box-shadow: 0px 0px 1px rgba(0, 0, 0, 0.85);
}

.colorpicker-body .strip .overlay {
	height: 150px;
	pointer-events: none;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* marker zone */

.monaco-editor .peekview-widget .head .peekview-title .severity-icon {
	display: inline-block;
	vertical-align: text-top;
	margin-right: 4px;
}

.monaco-editor .marker-widget {
	text-overflow: ellipsis;
	white-space: nowrap;
}

.monaco-editor .marker-widget > .stale {
	opacity: 0.6;
	font-style: italic;
}

.monaco-editor .marker-widget .title {
	display: inline-block;
	padding-right: 5px;
}

.monaco-editor .marker-widget .descriptioncontainer {
	position: absolute;
	white-space: pre;
	user-select: text;
	-webkit-user-select: text;
	-ms-user-select: text;
	padding: 8px 12px 0 20px;
}

.monaco-editor .marker-widget .descriptioncontainer .message {
	display: flex;
	flex-direction: column;
}

.monaco-editor .marker-widget .descriptioncontainer .message .details {
	padding-left: 6px;
}

.monaco-editor .marker-widget .descriptioncontainer .message .source,
.monaco-editor .marker-widget .descriptioncontainer .message span.code {
	opacity: 0.6;
}

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link {
	opacity: 0.6;
	color: inherit;
}

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link:before {
	content: '(';
}

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link:after {
	content: ')';
}

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link > span {
	text-decoration: underline;
	/** Hack to force underline to show **/
	border-bottom: 1px solid transparent;
	text-underline-position: under;
}

.monaco-editor .marker-widget .descriptioncontainer .filename {
	cursor: pointer;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .snippet-placeholder {
	min-width: 2px;
	outline-style: solid;
	outline-width: 1px;
}

.monaco-editor .finish-snippet-placeholder {
	outline-style: solid;
	outline-width: 1px;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

@font-face {
	font-family: "codicon";
	font-display: block;
	src: url(https://static-files.codility.com/prod/new-cui/aeb98e0beefa59d80a39.ttf) format("truetype");
}

.codicon[class*='codicon-'] {
	font: normal normal normal 16px/1 codicon;
	display: inline-block;
	text-decoration: none;
	text-rendering: auto;
	text-align: center;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

/* icon rules are dynamically created in codiconStyles */
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.codicon-wrench-subaction {
	opacity: 0.5;
}

@keyframes codicon-spin {
	100% {
		transform:rotate(360deg);
	}
}

.codicon-sync.codicon-modifier-spin,
.codicon-loading.codicon-modifier-spin,
.codicon-gear.codicon-modifier-spin,
.codicon-notebook-state-executing.codicon-modifier-spin {
	/* Use steps to throttle FPS to reduce CPU usage */
	animation: codicon-spin 1.5s steps(30) infinite;
}

.codicon-modifier-disabled {
	opacity: 0.4;
}

/* custom speed & easing for loading icon */
.codicon-loading,
.codicon-tree-item-loading::before {
	animation-duration: 1s !important;
	animation-timing-function: cubic-bezier(0.53, 0.21, 0.29, 0.67) !important;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Suggest widget*/

.monaco-editor .suggest-widget {
	width: 430px;
	z-index: 40;
	display: flex;
	flex-direction: column;
}

.monaco-editor .suggest-widget.message {
	flex-direction: row;
	align-items: center;
}

.monaco-editor .suggest-widget,
.monaco-editor .suggest-details {
	flex: 0 1 auto;
	width: 100%;
	border-style: solid;
	border-width: 1px;
}

.monaco-editor.hc-black .suggest-widget,
.monaco-editor.hc-black .suggest-details {
	border-width: 2px;
}

/* Styles for status bar part */


.monaco-editor .suggest-widget .suggest-status-bar {
	box-sizing: border-box;
	display: none;
	flex-flow: row nowrap;
	justify-content: space-between;
	width: 100%;
	font-size: 80%;
	padding: 0 4px 0 4px;
	border-top: 1px solid transparent;
	overflow: hidden;
}

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar {
	display: flex;
}

.monaco-editor .suggest-widget .suggest-status-bar .left {
	padding-right: 8px;
}

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar .action-label {
	opacity: 0.5;
	color: inherit;
}

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar .action-item:not(:last-of-type) .action-label {
	margin-right: 0;
}

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar .action-item:not(:last-of-type) .action-label::after {
	content: ', ';
	margin-right: 0.3em;
}

.monaco-editor .suggest-widget.with-status-bar .monaco-list .monaco-list-row>.contents>.main>.right>.readMore,
.monaco-editor .suggest-widget.with-status-bar .monaco-list .monaco-list-row.focused.string-label>.contents>.main>.right>.readMore {
	display: none;
}

.monaco-editor .suggest-widget.with-status-bar:not(.docs-side) .monaco-list .monaco-list-row:hover>.contents>.main>.right.can-expand-details>.details-label {
	width: 100%;
}

/* Styles for Message element for when widget is loading or is empty */

.monaco-editor .suggest-widget>.message {
	padding-left: 22px;
}

/** Styles for the list element **/

.monaco-editor .suggest-widget>.tree {
	height: 100%;
	width: 100%;
}

.monaco-editor .suggest-widget .monaco-list {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

/** Styles for each row in the list element **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row {
	display: flex;
	-mox-box-sizing: border-box;
	box-sizing: border-box;
	padding-right: 10px;
	background-repeat: no-repeat;
	background-position: 2px 2px;
	white-space: nowrap;
	cursor: pointer;
	touch-action: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents {
	flex: 1;
	height: 100%;
	overflow: hidden;
	padding-left: 2px;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main {
	display: flex;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: pre;
	justify-content: space-between;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.left, .monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right {
	display: flex;
}

.monaco-editor .suggest-widget:not(.frozen) .monaco-highlighted-label .highlight {
	font-weight: bold;
}

/** ReadMore Icon styles **/

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.header>.codicon-close,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.readMore::before {
	color: inherit;
	opacity: 1;
	font-size: 14px;
	cursor: pointer;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.header>.codicon-close {
	position: absolute;
	top: 6px;
	right: 2px;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.header>.codicon-close:hover,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.readMore:hover {
	opacity: 1;
}

/** signature, qualifier, type/details opacity **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.details-label {
	opacity: 0.7;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.left>.signature-label {
	overflow: hidden;
	text-overflow: ellipsis;
	opacity: 0.6;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.left>.qualifier-label {
	margin-left: 12px;
	opacity: 0.4;
	font-size: 85%;
	line-height: initial;
	text-overflow: ellipsis;
	overflow: hidden;
	align-self: center;
}

/** Type Info and icon next to the label in the focused completion item **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.details-label {
	font-size: 85%;
	margin-left: 1.1em;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.details-label>.monaco-tokenized-source {
	display: inline;
}

/** Details: if using CompletionItem#details, show on focus **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.details-label {
	display: none;
}

.monaco-editor .suggest-widget:not(.shows-details) .monaco-list .monaco-list-row.focused>.contents>.main>.right>.details-label {
	display: inline;
}

/** Details: if using CompletionItemLabel#details, always show **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row:not(.string-label)>.contents>.main>.right>.details-label,
.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row.focused:not(.string-label)>.contents>.main>.right>.details-label {
	display: inline;
}

/** Ellipsis on hover **/

.monaco-editor .suggest-widget:not(.docs-side) .monaco-list .monaco-list-row:hover>.contents>.main>.right.can-expand-details>.details-label {
	width: calc(100% - 26px);
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.left {
	flex-shrink: 1;
	flex-grow: 1;
	overflow: hidden;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.left>.monaco-icon-label {
	flex-shrink: 0;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row:not(.string-label)>.contents>.main>.left>.monaco-icon-label {
	max-width: 100%;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.string-label>.contents>.main>.left>.monaco-icon-label {
	flex-shrink: 1;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right {
	overflow: hidden;
	flex-shrink: 4;
	max-width: 70%;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row>.contents>.main>.right>.readMore {
	display: inline-block;
	position: absolute;
	right: 10px;
	width: 18px;
	height: 18px;
	visibility: hidden;
}

/** Do NOT display ReadMore when docs is side/below **/

.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row>.contents>.main>.right>.readMore, .monaco-editor .suggest-widget.docs-below .monaco-list .monaco-list-row>.contents>.main>.right>.readMore {
	display: none !important;
}

/** Do NOT display ReadMore when using plain CompletionItemLabel (details/documentation might not be resolved) **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.string-label>.contents>.main>.right>.readMore {
	display: none;
}

/** Focused item can show ReadMore, but can't when docs is side/below **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused.string-label>.contents>.main>.right>.readMore {
	display: inline-block;
}

.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row>.contents>.main>.right>.readMore,
.monaco-editor .suggest-widget.docs-below .monaco-list .monaco-list-row>.contents>.main>.right>.readMore {
	display: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row:hover>.contents>.main>.right>.readMore {
	visibility: visible;
}

/** Styles for each row in the list **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-icon-label.deprecated {
	opacity: 0.66;
	text-decoration: unset;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-icon-label.deprecated>.monaco-icon-label-container>.monaco-icon-name-container {
	text-decoration: line-through;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-icon-label::before {
	height: 100%;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon {
	display: block;
	height: 16px;
	width: 16px;
	margin-left: 2px;
	background-repeat: no-repeat;
	background-size: 80%;
	background-position: center;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.hide {
	display: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .suggest-icon {
	display: flex;
	align-items: center;
	margin-right: 4px;
}

.monaco-editor .suggest-widget.no-icons .monaco-list .monaco-list-row .icon, .monaco-editor .suggest-widget.no-icons .monaco-list .monaco-list-row .suggest-icon::before {
	display: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.customcolor .colorspan {
	margin: 0 0 0 0.3em;
	border: 0.1em solid #000;
	width: 0.7em;
	height: 0.7em;
	display: inline-block;
}

/** Styles for the docs of the completion item in focus **/

.monaco-editor .suggest-details-container {
	z-index: 41;
}

.monaco-editor .suggest-details {
	display: flex;
	flex-direction: column;
	cursor: default;
}

.monaco-editor .suggest-details.no-docs {
	display: none;
}

.monaco-editor .suggest-details>.monaco-scrollable-element {
	flex: 1;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body {
	box-sizing: border-box;
	height: 100%;
	width: 100%;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.header>.type {
	flex: 2;
	overflow: hidden;
	text-overflow: ellipsis;
	opacity: 0.7;
	white-space: pre;
	margin: 0 24px 0 0;
	padding: 4px 0 12px 5px;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.header>.type.auto-wrap {
	white-space: normal;
	word-break: break-all;
}


.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs {
	margin: 0;
	padding: 4px 5px;
	white-space: pre-wrap;
}

.monaco-editor .suggest-details.no-type>.monaco-scrollable-element>.body>.docs {
	margin-right: 24px;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs {
	padding: 0;
	white-space: initial;
	min-height: calc(1rem + 8px);
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs>div,
.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs>span:not(:empty) {
	padding: 4px 5px;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs>div>p:first-child {
	margin-top: 0;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs>div>p:last-child {
	margin-bottom: 0;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs .code {
	white-space: pre-wrap;
	word-wrap: break-word;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>.docs.markdown-docs .codicon {
	vertical-align: sub;
}

.monaco-editor .suggest-details>.monaco-scrollable-element>.body>p:empty {
	display: none;
}

.monaco-editor .suggest-details code {
	border-radius: 3px;
	padding: 0 0.4em;
}

.monaco-editor .suggest-details ul {
	padding-left: 20px;
}

.monaco-editor .suggest-details ol {
	padding-left: 20px;
}

.monaco-editor .suggest-details p code {
	font-family: var(--monaco-monospace-font);
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .suggest-preview-additional-widget {
	white-space: nowrap;
}

.monaco-editor .suggest-preview-additional-widget .content-spacer {
	color: transparent;
	white-space: pre;
}

.monaco-editor .suggest-preview-additional-widget .button {
	display: inline-block;
	cursor: pointer;
	text-decoration: underline;
	text-underline-position: under;
}

.monaco-editor .ghost-text-hidden {
	opacity: 0;
	font-size: 0;
}

.monaco-editor .ghost-text-decoration {
	font-style: italic;
}

.monaco-editor .suggest-preview-text {
	font-style: italic;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor.vs .dnd-target {
	border-right: 2px dotted black;
	color: white; /* opposite of black */
}
.monaco-editor.vs-dark .dnd-target {
	border-right: 2px dotted #AEAFAD;
	color: #51504f; /* opposite of #AEAFAD */
}
.monaco-editor.hc-black .dnd-target {
	border-right: 2px dotted #fff;
	color: #000; /* opposite of #fff */
}

.monaco-editor.mouse-default .view-lines,
.monaco-editor.vs-dark.mac.mouse-default .view-lines,
.monaco-editor.hc-black.mac.mouse-default .view-lines {
	cursor: default;
}
.monaco-editor.mouse-copy .view-lines,
.monaco-editor.vs-dark.mac.mouse-copy .view-lines,
.monaco-editor.hc-black.mac.mouse-copy .view-lines {
	cursor: copy;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-custom-checkbox {
	margin-left: 2px;
	float: left;
	cursor: pointer;
	overflow: hidden;
	opacity: 0.7;
	width: 20px;
	height: 20px;
	border: 1px solid transparent;
	padding: 1px;
	box-sizing:	border-box;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-custom-checkbox:hover,
.monaco-custom-checkbox.checked {
	opacity: 1;
}

.hc-black .monaco-custom-checkbox {
	background: none;
}

.hc-black .monaco-custom-checkbox:hover {
	background: none;
}

.monaco-custom-checkbox.monaco-simple-checkbox {
	height: 18px;
	width: 18px;
	border: 1px solid transparent;
	border-radius: 3px;
	margin-right: 9px;
	margin-left: 0px;
	padding: 0px;
	opacity: 1;
	background-size: 16px !important;
}

/* hide check when unchecked */
.monaco-custom-checkbox.monaco-simple-checkbox:not(.checked)::before {
	visibility: hidden;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Find widget */
.monaco-editor .find-widget {
	position: absolute;
	z-index: 35;
	height: 33px;
	overflow: hidden;
	line-height: 19px;
	transition: transform 200ms linear;
	padding: 0 4px;
	box-sizing: border-box;
	transform: translateY(calc(-100% - 10px)); /* shadow (10px) */
}

.monaco-editor .find-widget textarea {
	margin: 0px;
}

.monaco-editor .find-widget.hiddenEditor {
	display: none;
}

/* Find widget when replace is toggled on */
.monaco-editor .find-widget.replaceToggled > .replace-part {
	display: flex;
}

.monaco-editor .find-widget.visible  {
	transform: translateY(0);
}

.monaco-editor .find-widget .monaco-inputbox.synthetic-focus {
	outline: 1px solid -webkit-focus-ring-color;
	outline-offset: -1px;
}

.monaco-editor .find-widget .monaco-inputbox .input {
	background-color: transparent;
	min-height: 0;
}

.monaco-editor .find-widget .monaco-findInput .input {
	font-size: 13px;
}

.monaco-editor .find-widget > .find-part,
.monaco-editor .find-widget > .replace-part {
	margin: 4px 0 0 17px;
	font-size: 12px;
	display: flex;
}

.monaco-editor .find-widget > .find-part .monaco-inputbox,
.monaco-editor .find-widget > .replace-part .monaco-inputbox {
	min-height: 25px;
}


.monaco-editor .find-widget > .replace-part .monaco-inputbox > .ibwrapper > .mirror {
	padding-right: 22px;
}

.monaco-editor .find-widget > .find-part .monaco-inputbox > .ibwrapper > .input,
.monaco-editor .find-widget > .find-part .monaco-inputbox > .ibwrapper > .mirror,
.monaco-editor .find-widget > .replace-part .monaco-inputbox > .ibwrapper > .input,
.monaco-editor .find-widget > .replace-part .monaco-inputbox > .ibwrapper > .mirror {
	padding-top: 2px;
	padding-bottom: 2px;
}

.monaco-editor .find-widget > .find-part .find-actions {
	height: 25px;
	display: flex;
	align-items: center;
}

.monaco-editor .find-widget > .replace-part .replace-actions {
	height: 25px;
	display: flex;
	align-items: center;
}

.monaco-editor .find-widget .monaco-findInput {
	vertical-align: middle;
	display: flex;
	flex:1;
}

.monaco-editor .find-widget .monaco-findInput .monaco-scrollable-element {
	/* Make sure textarea inherits the width correctly */
	width: 100%;
}

.monaco-editor .find-widget .monaco-findInput .monaco-scrollable-element .scrollbar.vertical {
	/* Hide vertical scrollbar */
	opacity: 0;
}

.monaco-editor .find-widget .matchesCount {
	display: flex;
	flex: initial;
	margin: 0 0 0 3px;
	padding: 2px 0 0 2px;
	height: 25px;
	vertical-align: middle;
	box-sizing: border-box;
	text-align: center;
	line-height: 23px;
}

.monaco-editor .find-widget .button {
	width: 16px;
	height: 16px;
	padding: 3px;
	border-radius: 5px;
	display: flex;
	flex: initial;
	margin-left: 3px;
	background-position: center center;
	background-repeat: no-repeat;
	cursor: pointer;
	display: flex;
	align-items: center;
	justify-content: center;
}

/* find in selection button */
.monaco-editor .find-widget .codicon-find-selection {
	width: 22px;
	height: 22px;
	padding: 3px;
	border-radius: 5px;
}

.monaco-editor .find-widget .button.left {
	margin-left: 0;
	margin-right: 3px;
}

.monaco-editor .find-widget .button.wide {
	width: auto;
	padding: 1px 6px;
	top: -1px;
}

.monaco-editor .find-widget .button.toggle {
	position: absolute;
	top: 0;
	left: 3px;
	width: 18px;
	height: 100%;
	border-radius: 0;
	box-sizing: border-box;
}

.monaco-editor .find-widget .button.toggle.disabled {
	display: none;
}

.monaco-editor .find-widget .disabled {
	opacity: 0.3;
	cursor: default;
}

.monaco-editor .find-widget > .replace-part {
	display: none;
}

.monaco-editor .find-widget > .replace-part > .monaco-findInput {
	position: relative;
	display: flex;
	vertical-align: middle;
	flex: auto;
	flex-grow: 0;
	flex-shrink: 0;
}

.monaco-editor .find-widget > .replace-part > .monaco-findInput > .controls {
	position: absolute;
	top: 3px;
	right: 2px;
}

/* REDUCED */
.monaco-editor .find-widget.reduced-find-widget .matchesCount {
	display:none;
}

/* NARROW (SMALLER THAN REDUCED) */
.monaco-editor .find-widget.narrow-find-widget {
	max-width: 257px !important;
}

/* COLLAPSED (SMALLER THAN NARROW) */
.monaco-editor .find-widget.collapsed-find-widget {
	max-width: 170px !important;
}

.monaco-editor .find-widget.collapsed-find-widget .button.previous,
.monaco-editor .find-widget.collapsed-find-widget .button.next,
.monaco-editor .find-widget.collapsed-find-widget .button.replace,
.monaco-editor .find-widget.collapsed-find-widget .button.replace-all,
.monaco-editor .find-widget.collapsed-find-widget > .find-part .monaco-findInput .controls {
	display:none;
}

.monaco-editor .findMatch {
	animation-duration: 0;
	animation-name: inherit !important;
}

.monaco-editor .find-widget .monaco-sash {
	left: 0 !important;
}

.monaco-editor.hc-black .find-widget .button:before {
	position: relative;
	top: 1px;
	left: 2px;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-inputbox {
	position: relative;
	display: block;
	padding: 0;
	box-sizing:	border-box;

	/* Customizable */
	font-size: inherit;
}

.monaco-inputbox.idle {
	border: 1px solid transparent;
}

.monaco-inputbox > .ibwrapper > .input,
.monaco-inputbox > .ibwrapper > .mirror {

	/* Customizable */
	padding: 4px;
}

.monaco-inputbox > .ibwrapper {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-inputbox > .ibwrapper > .input {
	display: inline-block;
	box-sizing:	border-box;
	width: 100%;
	height: 100%;
	line-height: inherit;
	border: none;
	font-family: inherit;
	font-size: inherit;
	resize: none;
	color: inherit;
}

.monaco-inputbox > .ibwrapper > input {
	text-overflow: ellipsis;
}

.monaco-inputbox > .ibwrapper > textarea.input {
	display: block;
	-ms-overflow-style: none; /* IE 10+: hide scrollbars */
	scrollbar-width: none; /* Firefox: hide scrollbars */
	outline: none;
}

.monaco-inputbox > .ibwrapper > textarea.input::-webkit-scrollbar {
	display: none; /* Chrome + Safari: hide scrollbar */
}

.monaco-inputbox > .ibwrapper > textarea.input.empty {
	white-space: nowrap;
}

.monaco-inputbox > .ibwrapper > .mirror {
	position: absolute;
	display: inline-block;
	width: 100%;
	top: 0;
	left: 0;
	box-sizing: border-box;
	white-space: pre-wrap;
	visibility: hidden;
	word-wrap: break-word;
}

/* Context view */

.monaco-inputbox-container {
	text-align: right;
}

.monaco-inputbox-container .monaco-inputbox-message {
	display: inline-block;
	overflow: hidden;
	text-align: left;
	width: 100%;
	box-sizing:	border-box;
	padding: 0.4em;
	font-size: 12px;
	line-height: 17px;
	margin-top: -1px;
	word-wrap: break-word;
}

/* Action bar support */
.monaco-inputbox .monaco-action-bar {
	position: absolute;
	right: 2px;
	top: 4px;
}

.monaco-inputbox .monaco-action-bar .action-item {
	margin-left: 2px;
}

.monaco-inputbox .monaco-action-bar .action-item .codicon {
	background-repeat: no-repeat;
	width: 16px;
	height: 16px;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
/* ---------- Find input ---------- */

.monaco-findInput {
	position: relative;
}

.monaco-findInput .monaco-inputbox {
	font-size: 13px;
	width: 100%;
}

.monaco-findInput > .controls {
	position: absolute;
	top: 3px;
	right: 2px;
}

.vs .monaco-findInput.disabled {
	background-color: #E1E1E1;
}

/* Theming */
.vs-dark .monaco-findInput.disabled {
	background-color: #333;
}

/* Highlighting */
.monaco-findInput.highlight-0 .controls {
	animation: monaco-findInput-highlight-0 100ms linear 0s;
}
.monaco-findInput.highlight-1 .controls {
	animation: monaco-findInput-highlight-1 100ms linear 0s;
}
.hc-black .monaco-findInput.highlight-0 .controls,
.vs-dark  .monaco-findInput.highlight-0 .controls {
	animation: monaco-findInput-highlight-dark-0 100ms linear 0s;
}
.hc-black .monaco-findInput.highlight-1 .controls,
.vs-dark  .monaco-findInput.highlight-1 .controls {
	animation: monaco-findInput-highlight-dark-1 100ms linear 0s;
}

@keyframes monaco-findInput-highlight-0 {
	0% { background: rgba(253, 255, 0, 0.8); }
	100% { background: transparent; }
}
@keyframes monaco-findInput-highlight-1 {
	0% { background: rgba(253, 255, 0, 0.8); }
	/* Made intentionally different such that the CSS minifier does not collapse the two animations into a single one*/
	99% { background: transparent; }
}

@keyframes monaco-findInput-highlight-dark-0 {
	0% { background: rgba(255, 255, 255, 0.44); }
	100% { background: transparent; }
}
@keyframes monaco-findInput-highlight-dark-1 {
	0% { background: rgba(255, 255, 255, 0.44); }
	/* Made intentionally different such that the CSS minifier does not collapse the two animations into a single one*/
	99% { background: transparent; }
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .margin-view-overlays .codicon-folding-expanded,
.monaco-editor .margin-view-overlays .codicon-folding-collapsed {
	cursor: pointer;
	opacity: 0;
	transition: opacity 0.5s;
	display: flex;
	align-items: center;
	justify-content: center;
	font-size: 140%;
	margin-left: 2px;
}

.monaco-editor .margin-view-overlays:hover .codicon,
.monaco-editor .margin-view-overlays .codicon.codicon-folding-collapsed,
.monaco-editor .margin-view-overlays .codicon.alwaysShowFoldIcons {
	opacity: 1;
}

.monaco-editor .inline-folded:after {
	color: grey;
	margin: 0.1em 0.2em 0 0.2em;
	content: "⋯";
	display: inline;
	line-height: 1em;
	cursor: pointer;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .iPadShowKeyboard {
	width: 58px;
	min-width: 0;
	height: 36px;
	min-height: 0;
	margin: 0;
	padding: 0;
	position: absolute;
	resize: none;
	overflow: hidden;
	background: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMiIGhlaWdodD0iMzYiIHZpZXdCb3g9IjAgMCA1MyAzNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwKSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNDguMDM2NCA0LjAxMDQySDQuMDA3NzlMNC4wMDc3OSAzMi4wMjg2SDQ4LjAzNjRWNC4wMTA0MlpNNC4wMDc3OSAwLjAwNzgxMjVDMS43OTcyMSAwLjAwNzgxMjUgMC4wMDUxODc5OSAxLjc5OTg0IDAuMDA1MTg3OTkgNC4wMTA0MlYzMi4wMjg2QzAuMDA1MTg3OTkgMzQuMjM5MiAxLjc5NzIxIDM2LjAzMTIgNC4wMDc3OSAzNi4wMzEySDQ4LjAzNjRDNTAuMjQ3IDM2LjAzMTIgNTIuMDM5IDM0LjIzOTIgNTIuMDM5IDMyLjAyODZWNC4wMTA0MkM1Mi4wMzkgMS43OTk4NCA1MC4yNDcgMC4wMDc4MTI1IDQ4LjAzNjQgMC4wMDc4MTI1SDQuMDA3NzlaTTguMDEwNDIgOC4wMTMwMkgxMi4wMTNWMTIuMDE1Nkg4LjAxMDQyVjguMDEzMDJaTTIwLjAxODIgOC4wMTMwMkgxNi4wMTU2VjEyLjAxNTZIMjAuMDE4MlY4LjAxMzAyWk0yNC4wMjA4IDguMDEzMDJIMjguMDIzNFYxMi4wMTU2SDI0LjAyMDhWOC4wMTMwMlpNMzYuMDI4NiA4LjAxMzAySDMyLjAyNlYxMi4wMTU2SDM2LjAyODZWOC4wMTMwMlpNNDAuMDMxMiA4LjAxMzAySDQ0LjAzMzlWMTIuMDE1Nkg0MC4wMzEyVjguMDEzMDJaTTE2LjAxNTYgMTYuMDE4Mkg4LjAxMDQyVjIwLjAyMDhIMTYuMDE1NlYxNi4wMTgyWk0yMC4wMTgyIDE2LjAxODJIMjQuMDIwOFYyMC4wMjA4SDIwLjAxODJWMTYuMDE4MlpNMzIuMDI2IDE2LjAxODJIMjguMDIzNFYyMC4wMjA4SDMyLjAyNlYxNi4wMTgyWk00NC4wMzM5IDE2LjAxODJWMjAuMDIwOEgzNi4wMjg2VjE2LjAxODJINDQuMDMzOVpNMTIuMDEzIDI0LjAyMzRIOC4wMTA0MlYyOC4wMjZIMTIuMDEzVjI0LjAyMzRaTTE2LjAxNTYgMjQuMDIzNEgzNi4wMjg2VjI4LjAyNkgxNi4wMTU2VjI0LjAyMzRaTTQ0LjAzMzkgMjQuMDIzNEg0MC4wMzEyVjI4LjAyNkg0NC4wMzM5VjI0LjAyMzRaIiBmaWxsPSIjNDI0MjQyIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDAiPgo8cmVjdCB3aWR0aD0iNTMiIGhlaWdodD0iMzYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) center center no-repeat;
	border: 4px solid #F6F6F6;
	border-radius: 4px;
}

.monaco-editor.vs-dark .iPadShowKeyboard {
	background: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMiIGhlaWdodD0iMzYiIHZpZXdCb3g9IjAgMCA1MyAzNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwKSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNDguMDM2NCA0LjAxMDQySDQuMDA3NzlMNC4wMDc3OSAzMi4wMjg2SDQ4LjAzNjRWNC4wMTA0MlpNNC4wMDc3OSAwLjAwNzgxMjVDMS43OTcyMSAwLjAwNzgxMjUgMC4wMDUxODc5OSAxLjc5OTg0IDAuMDA1MTg3OTkgNC4wMTA0MlYzMi4wMjg2QzAuMDA1MTg3OTkgMzQuMjM5MiAxLjc5NzIxIDM2LjAzMTIgNC4wMDc3OSAzNi4wMzEySDQ4LjAzNjRDNTAuMjQ3IDM2LjAzMTIgNTIuMDM5IDM0LjIzOTIgNTIuMDM5IDMyLjAyODZWNC4wMTA0MkM1Mi4wMzkgMS43OTk4NCA1MC4yNDcgMC4wMDc4MTI1IDQ4LjAzNjQgMC4wMDc4MTI1SDQuMDA3NzlaTTguMDEwNDIgOC4wMTMwMkgxMi4wMTNWMTIuMDE1Nkg4LjAxMDQyVjguMDEzMDJaTTIwLjAxODIgOC4wMTMwMkgxNi4wMTU2VjEyLjAxNTZIMjAuMDE4MlY4LjAxMzAyWk0yNC4wMjA4IDguMDEzMDJIMjguMDIzNFYxMi4wMTU2SDI0LjAyMDhWOC4wMTMwMlpNMzYuMDI4NiA4LjAxMzAySDMyLjAyNlYxMi4wMTU2SDM2LjAyODZWOC4wMTMwMlpNNDAuMDMxMiA4LjAxMzAySDQ0LjAzMzlWMTIuMDE1Nkg0MC4wMzEyVjguMDEzMDJaTTE2LjAxNTYgMTYuMDE4Mkg4LjAxMDQyVjIwLjAyMDhIMTYuMDE1NlYxNi4wMTgyWk0yMC4wMTgyIDE2LjAxODJIMjQuMDIwOFYyMC4wMjA4SDIwLjAxODJWMTYuMDE4MlpNMzIuMDI2IDE2LjAxODJIMjguMDIzNFYyMC4wMjA4SDMyLjAyNlYxNi4wMTgyWk00NC4wMzM5IDE2LjAxODJWMjAuMDIwOEgzNi4wMjg2VjE2LjAxODJINDQuMDMzOVpNMTIuMDEzIDI0LjAyMzRIOC4wMTA0MlYyOC4wMjZIMTIuMDEzVjI0LjAyMzRaTTE2LjAxNTYgMjQuMDIzNEgzNi4wMjg2VjI4LjAyNkgxNi4wMTU2VjI0LjAyMzRaTTQ0LjAzMzkgMjQuMDIzNEg0MC4wMzEyVjI4LjAyNkg0NC4wMzM5VjI0LjAyMzRaIiBmaWxsPSIjQzVDNUM1Ii8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDAiPgo8cmVjdCB3aWR0aD0iNTMiIGhlaWdodD0iMzYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) center center no-repeat;
	border: 4px solid #252526;
}</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .tokens-inspect-widget {
	z-index: 50;
	user-select: text;
	-webkit-user-select: text;
	-ms-user-select: text;
	padding: 10px;
}

.tokens-inspect-separator {
	height: 1px;
	border: 0;
}

.monaco-editor .tokens-inspect-widget .tm-token {
	font-family: var(--monaco-monospace-font);
}

.monaco-editor .tokens-inspect-widget .tm-token-length {
	font-weight: normal;
	font-size: 60%;
	float: right;
}

.monaco-editor .tokens-inspect-widget .tm-metadata-table {
	width: 100%;
}

.monaco-editor .tokens-inspect-widget .tm-metadata-value {
	font-family: var(--monaco-monospace-font);
	text-align: right;
}

.monaco-editor .tokens-inspect-widget .tm-token-type {
	font-family: var(--monaco-monospace-font);
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .detected-link,
.monaco-editor .detected-link-active {
	text-decoration: underline;
	text-underline-position: under;
}

.monaco-editor .detected-link-active {
	cursor: pointer;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .parameter-hints-widget {
	z-index: 10;
	display: flex;
	flex-direction: column;
	line-height: 1.5em;
}

.monaco-editor .parameter-hints-widget > .phwrapper {
	max-width: 440px;
	display: flex;
	flex-direction: row;
}

.monaco-editor .parameter-hints-widget.multiple {
	min-height: 3.3em;
	padding: 0;
}

.monaco-editor .parameter-hints-widget.visible {
	transition: left .05s ease-in-out;
}

.monaco-editor .parameter-hints-widget p,
.monaco-editor .parameter-hints-widget ul {
	margin: 8px 0;
}

.monaco-editor .parameter-hints-widget .monaco-scrollable-element,
.monaco-editor .parameter-hints-widget .body {
	display: flex;
	flex: 1;
	flex-direction: column;
	min-height: 100%;
}

.monaco-editor .parameter-hints-widget .signature {
	padding: 4px 5px;
}

.monaco-editor .parameter-hints-widget .docs {
	padding: 0 10px 0 5px;
	white-space: pre-wrap;
}

.monaco-editor .parameter-hints-widget .docs.empty {
	display: none;
}

.monaco-editor .parameter-hints-widget .docs .markdown-docs {
	white-space: initial;
}

.monaco-editor .parameter-hints-widget .docs .markdown-docs code {
	font-family: var(--monaco-monospace-font);
}

.monaco-editor .parameter-hints-widget .docs .code {
	white-space: pre-wrap;
}

.monaco-editor .parameter-hints-widget .docs code {
	border-radius: 3px;
	padding: 0 0.4em;
}

.monaco-editor .parameter-hints-widget .controls {
	display: none;
	flex-direction: column;
	align-items: center;
	min-width: 22px;
	justify-content: flex-end;
}

.monaco-editor .parameter-hints-widget.multiple .controls {
	display: flex;
	padding: 0 2px;
}

.monaco-editor .parameter-hints-widget.multiple .button {
	width: 16px;
	height: 16px;
	background-repeat: no-repeat;
	cursor: pointer;
}

.monaco-editor .parameter-hints-widget .button.previous {
	bottom: 24px;
}

.monaco-editor .parameter-hints-widget .overloads {
	text-align: center;
	height: 12px;
	line-height: 12px;
	opacity: 0.5;
	font-family: var(--monaco-monospace-font);
}

.monaco-editor .parameter-hints-widget .signature .parameter.active {
	font-weight: bold;
	text-decoration: underline;
}

.monaco-editor .parameter-hints-widget .documentation-parameter > .parameter {
	font-weight: bold;
	margin-right: 0.5em;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .rename-box {
	z-index: 100;
	color: inherit;
}

.monaco-editor .rename-box.preview {
	padding: 3px 3px 0 3px;
}

.monaco-editor .rename-box .rename-input {
	padding: 3px;
	width: calc(100% - 6px);
}

.monaco-editor .rename-box .rename-label {
	display: none;
	opacity: .8;
}

.monaco-editor .rename-box.preview .rename-label {
	display: inherit;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/


/* Default standalone editor fonts */
.monaco-editor {
	font-family: -apple-system, BlinkMacSystemFont, "Segoe WPC", "Segoe UI", "HelveticaNeue-Light", system-ui, "Ubuntu", "Droid Sans", sans-serif;
	--monaco-monospace-font: "SF Mono", Monaco, Menlo, Consolas, "Ubuntu Mono", "Liberation Mono", "DejaVu Sans Mono", "Courier New", monospace;
}

.monaco-menu .monaco-action-bar.vertical .action-item .action-menu-item:focus .action-label {
	stroke-width: 1.2px;
}

.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label,
.monaco-editor.hc-black .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label {
	stroke-width: 1.2px;
}

.monaco-hover p {
	margin: 0;
}

/* See https://github.com/microsoft/monaco-editor/issues/2168#issuecomment-780078600 */
.monaco-aria-container {
	position: absolute !important;
	top: 0; /* avoid being placed underneath a sibling element */
	height: 1px;
	width: 1px;
	margin: -1px;
	overflow: hidden;
	padding: 0;
	clip: rect(1px, 1px, 1px, 1px);
	clip-path: inset(50%);
}

/* The hc-black theme is already high contrast optimized */
.monaco-editor.hc-black {
	-ms-high-contrast-adjust: none;
}
/* In case the browser goes into high contrast mode and the editor is not configured with the hc-black theme */
@media screen and (-ms-high-contrast:active) {

	/* current line highlight */
	.monaco-editor.vs .view-overlays .current-line,
	.monaco-editor.vs-dark .view-overlays .current-line {
		border-color: windowtext !important;
		border-left: 0;
		border-right: 0;
	}

	/* view cursors */
	.monaco-editor.vs .cursor,
	.monaco-editor.vs-dark .cursor {
		background-color: windowtext !important;
	}
	/* dnd target */
	.monaco-editor.vs .dnd-target,
	.monaco-editor.vs-dark .dnd-target {
		border-color: windowtext !important;
	}

	/* selected text background */
	.monaco-editor.vs .selected-text,
	.monaco-editor.vs-dark .selected-text {
		background-color: highlight !important;
	}

	/* allow the text to have a transparent background. */
	.monaco-editor.vs .view-line,
	.monaco-editor.vs-dark .view-line {
		-ms-high-contrast-adjust: none;
	}

	/* text color */
	.monaco-editor.vs .view-line span,
	.monaco-editor.vs-dark .view-line span {
		color: windowtext !important;
	}
	/* selected text color */
	.monaco-editor.vs .view-line span.inline-selected-text,
	.monaco-editor.vs-dark .view-line span.inline-selected-text {
		color: highlighttext !important;
	}

	/* allow decorations */
	.monaco-editor.vs .view-overlays,
	.monaco-editor.vs-dark .view-overlays {
		-ms-high-contrast-adjust: none;
	}

	/* various decorations */
	.monaco-editor.vs .selectionHighlight,
	.monaco-editor.vs-dark .selectionHighlight,
	.monaco-editor.vs .wordHighlight,
	.monaco-editor.vs-dark .wordHighlight,
	.monaco-editor.vs .wordHighlightStrong,
	.monaco-editor.vs-dark .wordHighlightStrong,
	.monaco-editor.vs .reference-decoration,
	.monaco-editor.vs-dark .reference-decoration {
		border: 2px dotted highlight !important;
		background: transparent !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .rangeHighlight,
	.monaco-editor.vs-dark .rangeHighlight {
		background: transparent !important;
		border: 1px dotted activeborder !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .bracket-match,
	.monaco-editor.vs-dark .bracket-match {
		border-color: windowtext !important;
		background: transparent !important;
	}

	/* find widget */
	.monaco-editor.vs .findMatch,
	.monaco-editor.vs-dark .findMatch,
	.monaco-editor.vs .currentFindMatch,
	.monaco-editor.vs-dark .currentFindMatch {
		border: 2px dotted activeborder !important;
		background: transparent !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .find-widget,
	.monaco-editor.vs-dark .find-widget {
		border: 1px solid windowtext;
	}

	/* list - used by suggest widget */
	.monaco-editor.vs .monaco-list .monaco-list-row,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row {
		-ms-high-contrast-adjust: none;
		color: windowtext !important;
	}
	.monaco-editor.vs .monaco-list .monaco-list-row.focused,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row.focused {
		color: highlighttext !important;
		background-color: highlight !important;
	}
	.monaco-editor.vs .monaco-list .monaco-list-row:hover,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row:hover {
		background: transparent !important;
		border: 1px solid highlight;
		box-sizing: border-box;
	}

	/* scrollbars */
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar {
		-ms-high-contrast-adjust: none;
		background: background !important;
		border: 1px solid windowtext;
		box-sizing: border-box;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider {
		background: windowtext !important;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider:hover,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider:hover {
		background: highlight !important;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider.active,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider.active {
		background: highlight !important;
	}

	/* overview ruler */
	.monaco-editor.vs .decorationsOverviewRuler,
	.monaco-editor.vs-dark .decorationsOverviewRuler {
		opacity: 0;
	}

	/* minimap */
	.monaco-editor.vs .minimap,
	.monaco-editor.vs-dark .minimap {
		display: none;
	}

	/* squiggles */
	.monaco-editor.vs .squiggly-d-error,
	.monaco-editor.vs-dark .squiggly-d-error {
		background: transparent !important;
		border-bottom: 4px double #E47777;
	}
	.monaco-editor.vs .squiggly-c-warning,
	.monaco-editor.vs-dark .squiggly-c-warning {
		border-bottom: 4px double #71B771;
	}
	.monaco-editor.vs .squiggly-b-info,
	.monaco-editor.vs-dark .squiggly-b-info {
		border-bottom: 4px double #71B771;
	}
	.monaco-editor.vs .squiggly-a-hint,
	.monaco-editor.vs-dark .squiggly-a-hint {
		border-bottom: 4px double #6c6c6c;
	}

	/* contextmenu */
	.monaco-editor.vs .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label,
	.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label {
		-ms-high-contrast-adjust: none;
		color: highlighttext !important;
		background-color: highlight !important;
	}
	.monaco-editor.vs .monaco-menu .monaco-action-bar.vertical .action-menu-item:hover .action-label,
	.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:hover .action-label {
		-ms-high-contrast-adjust: none;
		background: transparent !important;
		border: 1px solid highlight;
		box-sizing: border-box;
	}

	/* diff editor */
	.monaco-diff-editor.vs .diffOverviewRuler,
	.monaco-diff-editor.vs-dark .diffOverviewRuler {
		display: none;
	}
	.monaco-editor.vs .line-insert,
	.monaco-editor.vs-dark .line-insert,
	.monaco-editor.vs .line-delete,
	.monaco-editor.vs-dark .line-delete {
		background: transparent !important;
		border: 1px solid highlight !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .char-insert,
	.monaco-editor.vs-dark .char-insert,
	.monaco-editor.vs .char-delete,
	.monaco-editor.vs-dark .char-delete {
		background: transparent !important;
	}
}

/*.monaco-editor.vs [tabindex="0"]:focus {
	outline: 1px solid rgba(0, 122, 204, 0.4);
	outline-offset: -1px;
	opacity: 1 !important;
}

.monaco-editor.vs-dark [tabindex="0"]:focus {
	outline: 1px solid rgba(14, 99, 156, 0.6);
	outline-offset: -1px;
	opacity: 1 !important;
}*/
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
/* ---------- DiffEditor ---------- */

.monaco-diff-editor .diffOverview {
	z-index: 9;
}

.monaco-diff-editor .diffOverview .diffViewport {
	z-index: 10;
}

/* colors not externalized: using transparancy on background */
.monaco-diff-editor.vs			.diffOverview { background: rgba(0, 0, 0, 0.03); }
.monaco-diff-editor.vs-dark		.diffOverview { background: rgba(255, 255, 255, 0.01); }

.monaco-scrollable-element.modified-in-monaco-diff-editor.vs		.scrollbar { background: rgba(0,0,0,0); }
.monaco-scrollable-element.modified-in-monaco-diff-editor.vs-dark	.scrollbar { background: rgba(0,0,0,0); }
.monaco-scrollable-element.modified-in-monaco-diff-editor.hc-black	.scrollbar { background: none; }

.monaco-scrollable-element.modified-in-monaco-diff-editor .slider {
	z-index: 10;
}
.modified-in-monaco-diff-editor				.slider.active { background: rgba(171, 171, 171, .4); }
.modified-in-monaco-diff-editor.hc-black	.slider.active { background: none; }

/* ---------- Diff ---------- */

.monaco-editor .insert-sign,
.monaco-diff-editor .insert-sign,
.monaco-editor .delete-sign,
.monaco-diff-editor .delete-sign {
	font-size: 11px !important;
	opacity: 0.7 !important;
	display: flex !important;
	align-items: center;
}
.monaco-editor.hc-black .insert-sign,
.monaco-diff-editor.hc-black .insert-sign,
.monaco-editor.hc-black .delete-sign,
.monaco-diff-editor.hc-black .delete-sign {
	opacity: 1;
}

.monaco-editor .inline-deleted-margin-view-zone {
	text-align: right;
}
.monaco-editor .inline-added-margin-view-zone {
	text-align: right;
}

/* ---------- Inline Diff ---------- */

.monaco-editor .view-zones .view-lines .view-line span {
	display: inline-block;
}

.monaco-editor .margin-view-zones .lightbulb-glyph:hover {
	cursor: pointer;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-diff-editor .diff-review-line-number {
	text-align: right;
	display: inline-block;
}

.monaco-diff-editor .diff-review {
	position: absolute;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-diff-editor .diff-review-summary {
	padding-left: 10px;
}

.monaco-diff-editor .diff-review-shadow {
	position: absolute;
}

.monaco-diff-editor .diff-review-row {
	white-space: pre;
}

.monaco-diff-editor .diff-review-table {
	display: table;
	min-width: 100%;
}

.monaco-diff-editor .diff-review-row {
	display: table-row;
	width: 100%;
}

.monaco-diff-editor .diff-review-spacer {
	display: inline-block;
	width: 10px;
	vertical-align: middle;
}

.monaco-diff-editor .diff-review-spacer > .codicon {
	font-size: 9px !important;
}

.monaco-diff-editor .diff-review-actions {
	display: inline-block;
	position: absolute;
	right: 10px;
	top: 2px;
}

.monaco-diff-editor .diff-review-actions .action-label {
	width: 16px;
	height: 16px;
	margin: 2px 0;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.context-view {
	position: absolute;
	z-index: 2500;
}

.context-view.fixed {
	all: initial;
	font-family: inherit;
	font-size: 13px;
	position: fixed;
	z-index: 2500;
	color: inherit;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.context-view .monaco-menu {
	min-width: 130px;
}

</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.quick-input-widget {
	font-size: 13px;
}

.quick-input-widget .monaco-highlighted-label .highlight,
.quick-input-widget .monaco-highlighted-label .highlight {
	color: #0066BF;
}

.vs .quick-input-widget .monaco-list-row.focused .monaco-highlighted-label .highlight,
.vs .quick-input-widget .monaco-list-row.focused .monaco-highlighted-label .highlight {
	color: #9DDDFF;
}

.vs-dark .quick-input-widget .monaco-highlighted-label .highlight,
.vs-dark .quick-input-widget .monaco-highlighted-label .highlight {
	color: #0097fb;
}

.hc-black .quick-input-widget .monaco-highlighted-label .highlight,
.hc-black .quick-input-widget .monaco-highlighted-label .highlight {
	color: #F38518;
}

.monaco-keybinding > .monaco-keybinding-key {
	background-color: rgba(221, 221, 221, 0.4);
	border: solid 1px rgba(204, 204, 204, 0.4);
	border-bottom-color: rgba(187, 187, 187, 0.4);
	box-shadow: inset 0 -1px 0 rgba(187, 187, 187, 0.4);
	color: #555;
}

.hc-black .monaco-keybinding > .monaco-keybinding-key {
	background-color: transparent;
	border: solid 1px rgb(111, 195, 223);
	box-shadow: none;
	color: #fff;
}

.vs-dark .monaco-keybinding > .monaco-keybinding-key {
	background-color: rgba(128, 128, 128, 0.17);
	border: solid 1px rgba(51, 51, 51, 0.6);
	border-bottom-color: rgba(68, 68, 68, 0.6);
	box-shadow: inset 0 -1px 0 rgba(68, 68, 68, 0.6);
	color: #ccc;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-text-button {
	box-sizing: border-box;
	display: flex;
	width: 100%;
	padding: 4px;
	text-align: center;
	cursor: pointer;
	justify-content: center;
	align-items: center;
}

.monaco-text-button:focus {
	outline-offset: 2px !important;
}

.monaco-text-button:hover {
	text-decoration: none !important;
}

.monaco-button.disabled:focus,
.monaco-button.disabled {
	opacity: 0.4 !important;
	cursor: default;
}

.monaco-text-button > .codicon {
	margin: 0 0.2em;
	color: inherit !important;
}

.monaco-button-dropdown {
	display: flex;
	cursor: pointer;
}

.monaco-button-dropdown > .monaco-dropdown-button {
	margin-left: 1px;
}

.monaco-description-button {
	flex-direction: column;
}

.monaco-description-button .monaco-button-label {
	font-weight: 500;
}

.monaco-description-button .monaco-button-description {
	font-style: italic;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-progress-container {
	width: 100%;
	height: 5px;
	overflow: hidden; /* keep progress bit in bounds */
}

.monaco-progress-container .progress-bit {
	width: 2%;
	height: 5px;
	position: absolute;
	left: 0;
	display: none;
}

.monaco-progress-container.active .progress-bit {
	display: inherit;
}

.monaco-progress-container.discrete .progress-bit {
	left: 0;
	transition: width 100ms linear;
}

.monaco-progress-container.discrete.done .progress-bit {
	width: 100%;
}

.monaco-progress-container.infinite .progress-bit {
	animation-name: progress;
	animation-duration: 4s;
	animation-iteration-count: infinite;
	animation-timing-function: linear;
	transform: translate3d(0px, 0px, 0px);
}

/**
 * The progress bit has a width: 2% (1/50) of the parent container. The animation moves it from 0% to 100% of
 * that container. Since translateX is relative to the progress bit size, we have to multiple it with
 * its relative size to the parent container:
 * parent width: 5000%
 *    bit width: 100%
 * translateX should be as follow:
 *  50%: 5000% * 50% - 50% (set to center) = 2450%
 * 100%: 5000% * 100% - 100% (do not overflow) = 4900%
 */
@keyframes progress { from { transform: translateX(0%) scaleX(1) } 50% { transform: translateX(2500%) scaleX(3) } to { transform: translateX(4900%) scaleX(1) } }
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.quick-input-widget {
	position: absolute;
	width: 600px;
	z-index: 2000;
	padding: 0 1px 1px 1px;
	left: 50%;
	margin-left: -300px;
}

.quick-input-titlebar {
	display: flex;
	align-items: center;
}

.quick-input-left-action-bar {
	display: flex;
	margin-left: 4px;
	flex: 1;
}

.quick-input-title {
	padding: 3px 0px;
	text-align: center;
	text-overflow: ellipsis;
	overflow: hidden;
}

.quick-input-right-action-bar {
	display: flex;
	margin-right: 4px;
	flex: 1;
}

.quick-input-right-action-bar > .actions-container {
	justify-content: flex-end;
}

.quick-input-titlebar .monaco-action-bar .action-label.codicon {
	background-position: center;
	background-repeat: no-repeat;
	padding: 2px;
}

.quick-input-description {
	margin: 6px;
}

.quick-input-header .quick-input-description {
	margin: 4px 2px;
}

.quick-input-header {
	display: flex;
	padding: 6px 6px 0px 6px;
	margin-bottom: -2px;
}

.quick-input-widget.hidden-input .quick-input-header {
	/* reduce margins and paddings when input box hidden */
	padding: 0;
	margin-bottom: 0;
}

.quick-input-and-message {
	display: flex;
	flex-direction: column;
	flex-grow: 1;
	min-width: 0;
	position: relative;
}

.quick-input-check-all {
	align-self: center;
	margin: 0;
}

.quick-input-filter {
	flex-grow: 1;
	display: flex;
	position: relative;
}

.quick-input-box {
	flex-grow: 1;
}

.quick-input-widget.show-checkboxes .quick-input-box,
.quick-input-widget.show-checkboxes .quick-input-message {
	margin-left: 5px;
}

.quick-input-visible-count {
	position: absolute;
	left: -10000px;
}

.quick-input-count {
	align-self: center;
	position: absolute;
	right: 4px;
	display: flex;
	align-items: center;
}

.quick-input-count .monaco-count-badge {
	vertical-align: middle;
	padding: 2px 4px;
	border-radius: 2px;
	min-height: auto;
	line-height: normal;
}

.quick-input-action {
	margin-left: 6px;
}

.quick-input-action .monaco-text-button {
	font-size: 11px;
	padding: 0 6px;
	display: flex;
	height: 27.5px;
	align-items: center;
}

.quick-input-message {
	margin-top: -1px;
	padding: 5px 5px 2px 5px;
	overflow-wrap: break-word;
}

.quick-input-message > .codicon {
	margin: 0 0.2em;
	vertical-align: text-bottom;
}

.quick-input-progress.monaco-progress-container {
	position: relative;
}

.quick-input-progress.monaco-progress-container,
.quick-input-progress.monaco-progress-container .progress-bit {
	height: 2px;
}

.quick-input-list {
	line-height: 22px;
	margin-top: 6px;
}

.quick-input-widget.hidden-input .quick-input-list {
	margin-top: 0; /* reduce margins when input box hidden */
}

.quick-input-list .monaco-list {
	overflow: hidden;
	max-height: calc(20 * 22px);
}

.quick-input-list .quick-input-list-entry {
	box-sizing: border-box;
	overflow: hidden;
	display: flex;
	height: 100%;
	padding: 0 6px;
}

.quick-input-list .quick-input-list-entry.quick-input-list-separator-border {
	border-top-width: 1px;
	border-top-style: solid;
}

.quick-input-list .monaco-list-row[data-index="0"] .quick-input-list-entry.quick-input-list-separator-border {
	border-top-style: none;
}

.quick-input-list .quick-input-list-label {
	overflow: hidden;
	display: flex;
	height: 100%;
	flex: 1;
}

.quick-input-list .quick-input-list-checkbox {
	align-self: center;
	margin: 0;
}

.quick-input-list .quick-input-list-rows {
	overflow: hidden;
	text-overflow: ellipsis;
	display: flex;
	flex-direction: column;
	height: 100%;
	flex: 1;
	margin-left: 5px;
}

.quick-input-widget.show-checkboxes .quick-input-list .quick-input-list-rows {
	margin-left: 10px;
}

.quick-input-widget .quick-input-list .quick-input-list-checkbox {
	display: none;
}
.quick-input-widget.show-checkboxes .quick-input-list .quick-input-list-checkbox {
	display: inline;
}

.quick-input-list .quick-input-list-rows > .quick-input-list-row {
	display: flex;
	align-items: center;
}

.quick-input-list .quick-input-list-rows > .quick-input-list-row .monaco-icon-label,
.quick-input-list .quick-input-list-rows > .quick-input-list-row .monaco-icon-label .monaco-icon-label-container > .monaco-icon-name-container {
	flex: 1; /* make sure the icon label grows within the row */
}

.quick-input-list .quick-input-list-rows > .quick-input-list-row .codicon[class*='codicon-'] {
	vertical-align: text-bottom;
}

.quick-input-list .quick-input-list-rows .monaco-highlighted-label span {
	opacity: 1;
}

.quick-input-list .quick-input-list-entry .quick-input-list-entry-keybinding {
	margin-right: 8px; /* separate from the separator label or scrollbar if any */
}

.quick-input-list .quick-input-list-label-meta {
	opacity: 0.7;
	line-height: normal;
	text-overflow: ellipsis;
	overflow: hidden;
}

.quick-input-list .monaco-highlighted-label .highlight {
	font-weight: bold;
}

.quick-input-list .quick-input-list-entry .quick-input-list-separator {
	margin-right: 8px; /* separate from keybindings or actions */
}

.quick-input-list .quick-input-list-entry-action-bar {
	display: flex;
	flex: 0;
	overflow: visible;
}

.quick-input-list .quick-input-list-entry-action-bar .action-label {
	/*
	 * By default, actions in the quick input action bar are hidden
	 * until hovered over them or selected.
	 */
	display: none;
}

.quick-input-list .quick-input-list-entry-action-bar .action-label.codicon {
	margin-right: 4px;
	padding: 0px 2px 2px 2px;
}

.quick-input-list .quick-input-list-entry-action-bar {
	margin-top: 1px;
}

.quick-input-list .quick-input-list-entry-action-bar {
	margin-right: 4px; /* separate from scrollbar */
}

.quick-input-list .quick-input-list-entry .quick-input-list-entry-action-bar .action-label.always-visible,
.quick-input-list .quick-input-list-entry:hover .quick-input-list-entry-action-bar .action-label,
.quick-input-list .monaco-list-row.focused .quick-input-list-entry-action-bar .action-label {
	display: flex;
}

/* focused items in quick pick */
.quick-input-list .monaco-list-row.focused .monaco-keybinding-key,
.quick-input-list .monaco-list-row.focused .quick-input-list-entry .quick-input-list-separator {
	color: inherit
}
.quick-input-list .monaco-list-row.focused .monaco-keybinding-key {
	background: none;
}
</style><style>/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-keybinding {
	display: flex;
	align-items: center;
	line-height: 10px;
}

.monaco-keybinding > .monaco-keybinding-key {
	display: inline-block;
	border-style: solid;
	border-width: 1px;
	border-radius: 3px;
	vertical-align: middle;
	font-size: 11px;
	padding: 3px 5px;
	margin: 0 2px;
}

.monaco-keybinding > .monaco-keybinding-key:first-child {
	margin-left: 0;
}

.monaco-keybinding > .monaco-keybinding-key:last-child {
	margin-right: 0;
}

.monaco-keybinding > .monaco-keybinding-key-separator {
	display: inline-block;
}

.monaco-keybinding > .monaco-keybinding-key-chord-separator {
	width: 6px;
}
</style><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.monaco-editor .accessibilityHelpWidget { background-color: #252526; }
.monaco-editor .accessibilityHelpWidget { color: #cccccc; }
.monaco-editor .accessibilityHelpWidget { box-shadow: 0 2px 8px rgba(0, 0, 0, 0.36); }
.monaco-editor, .monaco-editor-background, .monaco-editor .inputarea.ime-input { background-color: #23241f; }
.monaco-editor, .monaco-editor .inputarea.ime-input { color: #d4d4d4; }
.monaco-editor .margin { background-color: #23241f; }
.monaco-editor .rangeHighlight { background-color: rgba(255, 255, 255, 0.04); }
.monaco-editor .symbolHighlight { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .mtkw { color: rgba(227, 228, 226, 0.16) !important; }
.monaco-editor .mtkz { color: rgba(227, 228, 226, 0.16) !important; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #ffd700; }
.monaco-editor .bracket-highlighting-1 { color: #da70d6; }
.monaco-editor .bracket-highlighting-2 { color: #179fff; }
.monaco-editor .bracket-highlighting-3 { color: #ffd700; }
.monaco-editor .bracket-highlighting-4 { color: #da70d6; }
.monaco-editor .bracket-highlighting-5 { color: #179fff; }
.monaco-editor .bracket-highlighting-6 { color: #ffd700; }
.monaco-editor .bracket-highlighting-7 { color: #da70d6; }
.monaco-editor .bracket-highlighting-8 { color: #179fff; }
.monaco-editor .bracket-highlighting-9 { color: #ffd700; }
.monaco-editor .bracket-highlighting-10 { color: #da70d6; }
.monaco-editor .bracket-highlighting-11 { color: #179fff; }
.monaco-editor .bracket-highlighting-12 { color: #ffd700; }
.monaco-editor .bracket-highlighting-13 { color: #da70d6; }
.monaco-editor .bracket-highlighting-14 { color: #179fff; }
.monaco-editor .bracket-highlighting-15 { color: #ffd700; }
.monaco-editor .bracket-highlighting-16 { color: #da70d6; }
.monaco-editor .bracket-highlighting-17 { color: #179fff; }
.monaco-editor .bracket-highlighting-18 { color: #ffd700; }
.monaco-editor .bracket-highlighting-19 { color: #da70d6; }
.monaco-editor .bracket-highlighting-20 { color: #179fff; }
.monaco-editor .bracket-highlighting-21 { color: #ffd700; }
.monaco-editor .bracket-highlighting-22 { color: #da70d6; }
.monaco-editor .bracket-highlighting-23 { color: #179fff; }
.monaco-editor .bracket-highlighting-24 { color: #ffd700; }
.monaco-editor .bracket-highlighting-25 { color: #da70d6; }
.monaco-editor .bracket-highlighting-26 { color: #179fff; }
.monaco-editor .bracket-highlighting-27 { color: #ffd700; }
.monaco-editor .bracket-highlighting-28 { color: #da70d6; }
.monaco-editor .bracket-highlighting-29 { color: #179fff; }
.monaco-editor .bracket-match { background-color: rgba(0, 100, 0, 0.1); }
.monaco-editor .bracket-match { border: 1px solid #888888; }
.monaco-editor .monaco-editor-overlaymessage .anchor.below { border-top-color: #007acc; }
.monaco-editor .monaco-editor-overlaymessage .anchor.top { border-bottom-color: #007acc; }
.monaco-editor .monaco-editor-overlaymessage .message { border: 1px solid #007acc; }
.monaco-editor .monaco-editor-overlaymessage .message { background-color: #063b49; }

		.monaco-editor .contentWidgets .codicon.codicon-light-bulb {
			color: #ffcc00;
			background-color: rgba(35, 36, 31, 0.7);
		}

		.monaco-editor .contentWidgets .codicon.codicon-lightbulb-autofix {
			color: #75beff;
			background-color: rgba(35, 36, 31, 0.7);
		}
.monaco-editor .codelens-decoration { color: #999999; }
.monaco-editor .codelens-decoration .codicon { color: #999999; }
.monaco-editor .codelens-decoration > a:hover { color: #4e94ce !important; }
.monaco-editor .codelens-decoration > a:hover .codicon { color: #4e94ce !important; }
.monaco-editor .line-numbers { color: #9e9e9e; }
.monaco-editor .line-numbers.active-line-number { color: #c6c6c6; }
.monaco-editor .view-overlays .current-line { border: 2px solid #333333; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #333333; }
.monaco-editor .lines-content .core-guide-indent { box-shadow: 1px 0 0 0 #404040 inset; }
.monaco-editor .lines-content .core-guide-indent-active { box-shadow: 1px 0 0 0 #707070 inset; }
.monaco-editor .bracket-indent-guide.lvl-0 { opacity: 0.3; box-shadow: 1px 0 0 0 #ffd700 inset; }
.monaco-editor .bracket-indent-guide.lvl-1 { opacity: 0.3; box-shadow: 1px 0 0 0 #da70d6 inset; }
.monaco-editor .bracket-indent-guide.lvl-2 { opacity: 0.3; box-shadow: 1px 0 0 0 #179fff inset; }
.monaco-editor .bracket-indent-guide.lvl-3 { opacity: 0.3; box-shadow: 1px 0 0 0 #ffd700 inset; }
.monaco-editor .bracket-indent-guide.lvl-4 { opacity: 0.3; box-shadow: 1px 0 0 0 #da70d6 inset; }
.monaco-editor .bracket-indent-guide.lvl-5 { opacity: 0.3; box-shadow: 1px 0 0 0 #179fff inset; }
.monaco-editor .bracket-indent-guide.lvl-6 { opacity: 0.3; box-shadow: 1px 0 0 0 #ffd700 inset; }
.monaco-editor .bracket-indent-guide.lvl-7 { opacity: 0.3; box-shadow: 1px 0 0 0 #da70d6 inset; }
.monaco-editor .bracket-indent-guide.lvl-8 { opacity: 0.3; box-shadow: 1px 0 0 0 #179fff inset; }
.monaco-editor .bracket-indent-guide.lvl-9 { opacity: 0.3; box-shadow: 1px 0 0 0 #ffd700 inset; }
.monaco-editor .bracket-indent-guide.lvl-10 { opacity: 0.3; box-shadow: 1px 0 0 0 #da70d6 inset; }
.monaco-editor .bracket-indent-guide.lvl-11 { opacity: 0.3; box-shadow: 1px 0 0 0 #179fff inset; }
.monaco-editor .bracket-indent-guide.lvl-12 { opacity: 0.3; box-shadow: 1px 0 0 0 #ffd700 inset; }
.monaco-editor .bracket-indent-guide.lvl-13 { opacity: 0.3; box-shadow: 1px 0 0 0 #da70d6 inset; }
.monaco-editor .bracket-indent-guide.lvl-14 { opacity: 0.3; box-shadow: 1px 0 0 0 #179fff inset; }
.monaco-editor .bracket-indent-guide.lvl-15 { opacity: 0.3; box-shadow: 1px 0 0 0 #ffd700 inset; }
.monaco-editor .bracket-indent-guide.lvl-16 { opacity: 0.3; box-shadow: 1px 0 0 0 #da70d6 inset; }
.monaco-editor .bracket-indent-guide.lvl-17 { opacity: 0.3; box-shadow: 1px 0 0 0 #179fff inset; }
.monaco-editor .bracket-indent-guide.lvl-18 { opacity: 0.3; box-shadow: 1px 0 0 0 #ffd700 inset; }
.monaco-editor .bracket-indent-guide.lvl-19 { opacity: 0.3; box-shadow: 1px 0 0 0 #da70d6 inset; }
.monaco-editor .bracket-indent-guide.lvl-20 { opacity: 0.3; box-shadow: 1px 0 0 0 #179fff inset; }
.monaco-editor .bracket-indent-guide.lvl-21 { opacity: 0.3; box-shadow: 1px 0 0 0 #ffd700 inset; }
.monaco-editor .bracket-indent-guide.lvl-22 { opacity: 0.3; box-shadow: 1px 0 0 0 #da70d6 inset; }
.monaco-editor .bracket-indent-guide.lvl-23 { opacity: 0.3; box-shadow: 1px 0 0 0 #179fff inset; }
.monaco-editor .bracket-indent-guide.lvl-24 { opacity: 0.3; box-shadow: 1px 0 0 0 #ffd700 inset; }
.monaco-editor .bracket-indent-guide.lvl-25 { opacity: 0.3; box-shadow: 1px 0 0 0 #da70d6 inset; }
.monaco-editor .bracket-indent-guide.lvl-26 { opacity: 0.3; box-shadow: 1px 0 0 0 #179fff inset; }
.monaco-editor .bracket-indent-guide.lvl-27 { opacity: 0.3; box-shadow: 1px 0 0 0 #ffd700 inset; }
.monaco-editor .bracket-indent-guide.lvl-28 { opacity: 0.3; box-shadow: 1px 0 0 0 #da70d6 inset; }
.monaco-editor .bracket-indent-guide.lvl-29 { opacity: 0.3; box-shadow: 1px 0 0 0 #179fff inset; }
.monaco-editor .indent-active { opacity: 1 !important; }
.monaco-editor .minimap-slider .minimap-slider-horizontal { background: rgba(121, 121, 121, 0.2); }
.monaco-editor .minimap-slider:hover .minimap-slider-horizontal { background: rgba(100, 100, 100, 0.35); }
.monaco-editor .minimap-slider.active .minimap-slider-horizontal { background: rgba(191, 191, 191, 0.2); }
.monaco-editor .minimap-shadow-visible { box-shadow: #000000 -6px 0 6px -6px inset; }
.monaco-editor .view-ruler { box-shadow: 1px 0 0 0 #5a5a5a inset; }
.monaco-editor .scroll-decoration { box-shadow: #000000 0 6px 6px -6px inset; }
.monaco-editor .focused .selected-text { background-color: #264f78; }
.monaco-editor .selected-text { background-color: #3a3d41; }
.monaco-editor .cursors-layer .cursor { background-color: #aeafad; border-color: #aeafad; color: #515052; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23f14c4c'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23cca700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%233794ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22rgba(238%2C%20238%2C%20238%2C%200.7)%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.667; }
.monaco-editor.showDeprecated .squiggly-inline-deprecated { text-decoration: line-through; text-decoration-color: #d4d4d4}
.monaco-editor .reference-zone-widget .ref-tree .referenceMatch .highlight { background-color: rgba(234, 92, 0, 0.3); }
.monaco-editor .reference-zone-widget .preview .reference-decoration { background-color: rgba(255, 143, 0, 0.6); }
.monaco-editor .reference-zone-widget .ref-tree { background-color: #252526; }
.monaco-editor .reference-zone-widget .ref-tree { color: #bbbbbb; }
.monaco-editor .reference-zone-widget .ref-tree .reference-file { color: #ffffff; }
.monaco-editor .reference-zone-widget .ref-tree .monaco-list:focus .monaco-list-rows > .monaco-list-row.selected:not(.highlighted) { background-color: rgba(51, 153, 255, 0.2); }
.monaco-editor .reference-zone-widget .ref-tree .monaco-list:focus .monaco-list-rows > .monaco-list-row.selected:not(.highlighted) { color: #ffffff !important; }
.monaco-editor .reference-zone-widget .preview .monaco-editor .monaco-editor-background,.monaco-editor .reference-zone-widget .preview .monaco-editor .inputarea.ime-input {	background-color: #001f33;}
.monaco-editor .reference-zone-widget .preview .monaco-editor .margin {	background-color: #001f33;}
.monaco-editor .goto-definition-link { color: #4e94ce !important; }

			.monaco-editor .zone-widget .codicon.codicon-error,
			.markers-panel .marker-icon.codicon.codicon-error,
			.text-search-provider-messages .providerMessage .codicon.codicon-error,
			.extensions-viewlet > .extensions .codicon.codicon-error {
				color: #f14c4c;
			}
		

			.monaco-editor .zone-widget .codicon.codicon-warning,
			.markers-panel .marker-icon.codicon.codicon-warning,
			.extensions-viewlet > .extensions .codicon.codicon-warning,
			.extension-editor .codicon.codicon-warning,
			.text-search-provider-messages .providerMessage .codicon.codicon-warning,
			.preferences-editor .codicon.codicon-warning {
				color: #cca700;
			}
		

			.monaco-editor .zone-widget .codicon.codicon-info,
			.markers-panel .marker-icon.codicon.codicon-info,
			.extensions-viewlet > .extensions .codicon.codicon-info,
			.text-search-provider-messages .providerMessage .codicon.codicon-info,
			.extension-editor .codicon.codicon-info {
				color: #3794ff;
			}
		
.monaco-editor .marker-widget a.code-link span { color: #3794ff; }
.monaco-editor .marker-widget a.code-link span:hover { color: #3794ff; }
.monaco-hover .hover-contents a.code-link span { color: #3794ff; }
.monaco-hover .hover-contents a.code-link span:hover { color: #3794ff; }
.monaco-editor .snippet-placeholder { background-color: rgba(124, 124, 124, 0.3); outline-color: transparent; }
.monaco-editor .finish-snippet-placeholder { background-color: transparent; outline-color: #525252; }
.codicon.codicon-symbol-array { color: #cccccc; }
.codicon.codicon-symbol-boolean { color: #cccccc; }
.codicon.codicon-symbol-class { color: #ee9d28; }
.codicon.codicon-symbol-method { color: #b180d7; }
.codicon.codicon-symbol-color { color: #cccccc; }
.codicon.codicon-symbol-constant { color: #cccccc; }
.codicon.codicon-symbol-constructor { color: #b180d7; }

			.codicon.codicon-symbol-value,.codicon.codicon-symbol-enum { color: #ee9d28; }
.codicon.codicon-symbol-enum-member { color: #75beff; }
.codicon.codicon-symbol-event { color: #ee9d28; }
.codicon.codicon-symbol-field { color: #75beff; }
.codicon.codicon-symbol-file { color: #cccccc; }
.codicon.codicon-symbol-folder { color: #cccccc; }
.codicon.codicon-symbol-function { color: #b180d7; }
.codicon.codicon-symbol-interface { color: #75beff; }
.codicon.codicon-symbol-key { color: #cccccc; }
.codicon.codicon-symbol-keyword { color: #cccccc; }
.codicon.codicon-symbol-module { color: #cccccc; }
.codicon.codicon-symbol-namespace { color: #cccccc; }
.codicon.codicon-symbol-null { color: #cccccc; }
.codicon.codicon-symbol-number { color: #cccccc; }
.codicon.codicon-symbol-object { color: #cccccc; }
.codicon.codicon-symbol-operator { color: #cccccc; }
.codicon.codicon-symbol-package { color: #cccccc; }
.codicon.codicon-symbol-property { color: #cccccc; }
.codicon.codicon-symbol-reference { color: #cccccc; }
.codicon.codicon-symbol-snippet { color: #cccccc; }
.codicon.codicon-symbol-string { color: #cccccc; }
.codicon.codicon-symbol-struct { color: #cccccc; }
.codicon.codicon-symbol-text { color: #cccccc; }
.codicon.codicon-symbol-type-parameter { color: #cccccc; }
.codicon.codicon-symbol-unit { color: #cccccc; }
.codicon.codicon-symbol-variable { color: #75beff; }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-highlighted-label .highlight { color: #18a3ff; }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused .monaco-highlighted-label .highlight { color: #18a3ff; }
.monaco-editor .suggest-widget, .monaco-editor .suggest-details { color: #d4d4d4; }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused { color: #ffffff; }
.monaco-editor .suggest-details a { color: #3794ff; }
.monaco-editor .suggest-details a:hover { color: #3794ff; }
.monaco-editor .suggest-details code { background-color: rgba(10, 10, 10, 0.4); }
.monaco-editor .ghost-text-decoration { opacity: 0.337 !important; color: #ffffff !important; }
.monaco-editor .ghost-text-decoration-preview { color: rgba(255, 255, 255, 0.34) !important; }
.monaco-editor .suggest-preview-text .ghost-text { opacity: 0.337 !important; color: #ffffff !important; }
.monaco-editor .hoverHighlight { background-color: rgba(38, 79, 120, 0.25); }
.monaco-editor .monaco-hover { background-color: #252526; }
.monaco-editor .monaco-hover { border: 1px solid #454545; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover a { color: #3794ff; }
.monaco-editor .monaco-hover a:hover { color: #3794ff; }
.monaco-editor .monaco-hover { color: #cccccc; }
.monaco-editor .monaco-hover .hover-row .actions { background-color: #2c2c2d; }
.monaco-editor .monaco-hover code { background-color: rgba(10, 10, 10, 0.4); }
.monaco-editor .findOptionsWidget { background-color: #252526; }
.monaco-editor .findOptionsWidget { color: #cccccc; }
.monaco-editor .findOptionsWidget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #515c6a; }
.monaco-editor .findScope { background-color: rgba(58, 61, 65, 0.4); }
.monaco-editor .find-widget { background-color: #252526; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .find-widget { color: #cccccc; }
.monaco-editor .find-widget.no-results .matchesCount { color: #f48771; }
.monaco-editor .find-widget .monaco-sash { background-color: #454545; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(90, 93, 94, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #007fd4; }
.monaco-editor .folded-background { background-color: rgba(38, 79, 120, 0.3); }

		.monaco-editor .cldr.codicon.codicon-folding-expanded,
		.monaco-editor .cldr.codicon.codicon-folding-collapsed {
			color: #c5c5c5 !important;
		}
		
.monaco-editor.vs .valueSetReplacement { outline: solid 2px #888888; }
.monaco-editor .tokens-inspect-widget { border: 1px solid #454545; }
.monaco-editor .tokens-inspect-widget .tokens-inspect-separator { background-color: #454545; }
.monaco-editor .tokens-inspect-widget { background-color: #252526; }
.monaco-editor .tokens-inspect-widget { color: #cccccc; }
.monaco-editor .linked-editing-decoration { background: rgba(255, 0, 0, 0.3); border-left-color: rgba(255, 0, 0, 0.3); }
.monaco-editor .detected-link-active { color: #4e94ce !important; }
.monaco-editor .parameter-hints-widget { border: 1px solid #454545; }
.monaco-editor .parameter-hints-widget.multiple .body { border-left: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .parameter-hints-widget .signature.has-docs { border-bottom: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .parameter-hints-widget { background-color: #252526; }
.monaco-editor .parameter-hints-widget a { color: #3794ff; }
.monaco-editor .parameter-hints-widget a:hover { color: #3794ff; }
.monaco-editor .parameter-hints-widget { color: #cccccc; }
.monaco-editor .parameter-hints-widget code { background-color: rgba(10, 10, 10, 0.4); }
.monaco-editor .focused .selectionHighlight { background-color: rgba(173, 214, 255, 0.15); }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.07); }
.monaco-editor .wordHighlight { background-color: rgba(87, 87, 87, 0.72); }
.monaco-editor .wordHighlightStrong { background-color: rgba(0, 73, 114, 0.72); }
.monaco-diff-editor .diff-review-line-number { color: #9e9e9e; }
.monaco-diff-editor .diff-review-shadow { box-shadow: #000000 0 -6px 6px -6px inset; }
.monaco-editor .line-insert, .monaco-editor .char-insert { background-color: rgba(155, 185, 85, 0.2); }
.monaco-diff-editor .line-insert, .monaco-diff-editor .char-insert { background-color: rgba(155, 185, 85, 0.2); }
.monaco-editor .inline-added-margin-view-zone { background-color: rgba(155, 185, 85, 0.2); }
.monaco-editor .line-delete, .monaco-editor .char-delete { background-color: rgba(255, 0, 0, 0.2); }
.monaco-diff-editor .line-delete, .monaco-diff-editor .char-delete { background-color: rgba(255, 0, 0, 0.2); }
.monaco-editor .inline-deleted-margin-view-zone { background-color: rgba(255, 0, 0, 0.2); }
.monaco-diff-editor.side-by-side .editor.modified { box-shadow: -6px 0 5px -5px #000000; }

			.monaco-diff-editor .diffViewport {
				background: rgba(121, 121, 121, 0.4);
			}
		

			.monaco-diff-editor .diffViewport:hover {
				background: rgba(100, 100, 100, 0.7);
			}
		

			.monaco-diff-editor .diffViewport:active {
				background: rgba(191, 191, 191, 0.4);
			}
		

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(204, 204, 204, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(204, 204, 204, 0.2) 50%, rgba(204, 204, 204, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	

.mtk1 { color: #d4d4d4; }
.mtk2 { color: #ffffff; }
.mtk3 { color: #6a9955; }
.mtk4 { color: #569cd6; }
.mtk5 { color: #d16969; }
.mtk6 { color: #d7ba7d; }
.mtk7 { color: #b5cea8; }
.mtk8 { color: #ce9178; }
.mtk9 { color: #646695; }
.mtk10 { color: #4ec9b0; }
.mtk11 { color: #dcdcaa; }
.mtk12 { color: #c8c8c8; }
.mtk13 { color: #c586c0; }
.mtk14 { color: #9cdcfe; }
.mtk15 { color: #000080; }
.mtk16 { color: #f44747; }
.mtk17 { color: #6796e6; }
.mtk18 { color: #808080; }
.mtk19 { color: #b267e6; }
.mtk20 { color: #cd9731; }
.mtk21 { color: #4fc1ff; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }</style><style type="text/css" media="screen">
		.monaco-editor .codelens-decoration._ee1f62 { line-height: 19px; font-size: 12px; padding-right: 6px; font-feature-settings: var(--codelens-font-features_ee1f62) }
		.monaco-editor .codelens-decoration._ee1f62 span.codicon { line-height: 19px; font-size: 12px; }
		</style></head>

<body style=""><div id="skip-to-content-link-container"><a class="Button__LinkWrapper-sc-hbh4t9-2 cxinLu has-min-width SkipToContent__StyledButton-sc-qtir4r-0 eMbVtI" role="link" tabindex="0" href="https://app.codility.com/c/run/trainingR4ZZZF-PJE/#working-area-editor" target="_self" rel="noopener noreferrer">Skip to editor</a></div>
  
    <div id="js-ui-data" data-raw-ticket-id="&quot;trainingR4ZZZF-PJE&quot;" data-raw-ticket_id="&quot;trainingR4ZZZF-PJE&quot;" data-raw-prg_langs="{&quot;c&quot;: {&quot;name&quot;: &quot;C&quot;, &quot;label&quot;: &quot;C&quot;}, &quot;cpp&quot;: {&quot;name&quot;: &quot;C++&quot;, &quot;label&quot;: &quot;C plus plus&quot;}, &quot;cpp_20&quot;: {&quot;name&quot;: &quot;C++20&quot;, &quot;label&quot;: &quot;C plus plus&quot;}, &quot;cs&quot;: {&quot;name&quot;: &quot;C#&quot;, &quot;label&quot;: &quot;C sharp&quot;}, &quot;clj&quot;: {&quot;name&quot;: &quot;Clojure&quot;, &quot;label&quot;: &quot;Clojure&quot;}, &quot;dart&quot;: {&quot;name&quot;: &quot;Dart&quot;, &quot;label&quot;: &quot;Dart&quot;}, &quot;java&quot;: {&quot;name&quot;: &quot;Java 8&quot;, &quot;label&quot;: &quot;Java 8&quot;}, &quot;java11&quot;: {&quot;name&quot;: &quot;Java 11&quot;, &quot;label&quot;: &quot;Java 11&quot;}, &quot;js&quot;: {&quot;name&quot;: &quot;JavaScript&quot;, &quot;label&quot;: &quot;Java script&quot;}, &quot;lua&quot;: {&quot;name&quot;: &quot;Lua&quot;, &quot;label&quot;: &quot;Lua&quot;}, &quot;m&quot;: {&quot;name&quot;: &quot;Objective-C&quot;, &quot;label&quot;: &quot;Objective c&quot;}, &quot;py&quot;: {&quot;name&quot;: &quot;Python&quot;, &quot;label&quot;: &quot;Python&quot;}, &quot;pas&quot;: {&quot;name&quot;: &quot;Pascal&quot;, &quot;label&quot;: &quot;Pascal&quot;}, &quot;php&quot;: {&quot;name&quot;: &quot;PHP&quot;, &quot;label&quot;: &quot;PHP&quot;}, &quot;pl&quot;: {&quot;name&quot;: &quot;Perl&quot;, &quot;label&quot;: &quot;Perl&quot;}, &quot;rb&quot;: {&quot;name&quot;: &quot;Ruby&quot;, &quot;label&quot;: &quot;Ruby&quot;}, &quot;rs&quot;: {&quot;name&quot;: &quot;Rust&quot;, &quot;label&quot;: &quot;Rust&quot;}, &quot;scala&quot;: {&quot;name&quot;: &quot;Scala&quot;, &quot;label&quot;: &quot;Scala&quot;}, &quot;sql&quot;: {&quot;name&quot;: &quot;SQL (SQLite)&quot;, &quot;label&quot;: &quot;SQL (SQLite)&quot;}, &quot;sql-postgres&quot;: {&quot;name&quot;: &quot;SQL (PostgreSQL)&quot;, &quot;label&quot;: &quot;SQL (PostgreSQL)&quot;}, &quot;swift&quot;: {&quot;name&quot;: &quot;Swift&quot;, &quot;label&quot;: &quot;swift&quot;}, &quot;swift3&quot;: {&quot;name&quot;: &quot;Swift 3&quot;, &quot;label&quot;: &quot;Swift 3&quot;}, &quot;swift4&quot;: {&quot;name&quot;: &quot;Swift 4&quot;, &quot;label&quot;: &quot;Swift 4&quot;}, &quot;ts&quot;: {&quot;name&quot;: &quot;TypeScript&quot;, &quot;label&quot;: &quot;Type script&quot;}, &quot;vb&quot;: {&quot;name&quot;: &quot;Visual Basic&quot;, &quot;label&quot;: &quot;Visual basic dot net&quot;}, &quot;go&quot;: {&quot;name&quot;: &quot;Go&quot;, &quot;label&quot;: &quot;Go&quot;}, &quot;txt&quot;: {&quot;name&quot;: &quot;Text&quot;, &quot;label&quot;: &quot;Text&quot;}, &quot;mcq&quot;: {&quot;name&quot;: &quot;Multiple-choice questions&quot;, &quot;label&quot;: &quot;Multiple-choice questions&quot;}, &quot;file&quot;: {&quot;name&quot;: &quot;File upload&quot;, &quot;label&quot;: &quot;File upload&quot;}, &quot;regex&quot;: {&quot;name&quot;: &quot;Regular expression&quot;, &quot;label&quot;: &quot;Regular expression&quot;}, &quot;bash&quot;: {&quot;name&quot;: &quot;Bash&quot;, &quot;label&quot;: &quot;Bash&quot;}, &quot;robot&quot;: {&quot;name&quot;: &quot;Robot Framework&quot;, &quot;label&quot;: &quot;Robot Framework&quot;}, &quot;sol&quot;: {&quot;name&quot;: &quot;Solidity&quot;, &quot;label&quot;: &quot;Solidity&quot;}, &quot;erb&quot;: {&quot;name&quot;: &quot;Ruby Templates&quot;, &quot;label&quot;: &quot;Ruby Templates&quot;}, &quot;kt&quot;: {&quot;name&quot;: &quot;Kotlin&quot;, &quot;label&quot;: &quot;Kotlin&quot;}, &quot;R&quot;: {&quot;name&quot;: &quot;R&quot;, &quot;label&quot;: &quot;R&quot;}, &quot;yaml&quot;: {&quot;name&quot;: &quot;YAML&quot;, &quot;label&quot;: &quot;YAML&quot;}, &quot;tf&quot;: {&quot;name&quot;: &quot;Terraform&quot;, &quot;label&quot;: &quot;Terraform&quot;}, &quot;cbl&quot;: {&quot;name&quot;: &quot;Cobol&quot;, &quot;label&quot;: &quot;Cobol&quot;}, &quot;Dockerfile&quot;: {&quot;name&quot;: &quot;Dockerfile&quot;, &quot;label&quot;: &quot;Dockerfile&quot;}, &quot;mysql&quot;: {&quot;name&quot;: &quot;MySQL&quot;, &quot;label&quot;: &quot;MySQL&quot;}}" data-raw-human_langs="{&quot;en&quot;: {&quot;name&quot;: &quot;English&quot;, &quot;label&quot;: &quot;English&quot;, &quot;iso639Code&quot;: null}, &quot;cn&quot;: {&quot;name&quot;: &quot;\u4e2d\u6587&quot;, &quot;label&quot;: &quot;Chinese&quot;, &quot;iso639Code&quot;: &quot;zh&quot;}, &quot;pl&quot;: {&quot;name&quot;: &quot;Polski&quot;, &quot;label&quot;: &quot;Polish&quot;, &quot;iso639Code&quot;: null}, &quot;es&quot;: {&quot;name&quot;: &quot;Espa\u00f1ol&quot;, &quot;label&quot;: &quot;Spanish&quot;, &quot;iso639Code&quot;: null}, &quot;fr&quot;: {&quot;name&quot;: &quot;Fran\u00e7ais&quot;, &quot;label&quot;: &quot;French&quot;, &quot;iso639Code&quot;: null}, &quot;de&quot;: {&quot;name&quot;: &quot;Deutsch&quot;, &quot;label&quot;: &quot;German&quot;, &quot;iso639Code&quot;: null}, &quot;jp&quot;: {&quot;name&quot;: &quot;\u65e5\u672c\u8a9e&quot;, &quot;label&quot;: &quot;Japanese&quot;, &quot;iso639Code&quot;: &quot;ja&quot;}, &quot;ru&quot;: {&quot;name&quot;: &quot;\u0420\u0443\u0441\u0441\u043a\u0438\u0439&quot;, &quot;label&quot;: &quot;Russian&quot;, &quot;iso639Code&quot;: null}, &quot;pt-BR&quot;: {&quot;name&quot;: &quot;Brazilian Portuguese&quot;, &quot;label&quot;: &quot;Brazilian Portuguese&quot;, &quot;iso639Code&quot;: null}, &quot;kr&quot;: {&quot;name&quot;: &quot;\ud55c\uad6d\uc5b4&quot;, &quot;label&quot;: &quot;Korean&quot;, &quot;iso639Code&quot;: &quot;ko&quot;}, &quot;vi&quot;: {&quot;name&quot;: &quot;ti\u1ebfng Vi\u1ec7t&quot;, &quot;label&quot;: &quot;Vietnamese&quot;, &quot;iso639Code&quot;: &quot;vi&quot;}}" data-raw-show_support="false" data-raw-show_survey="false" data-raw-show_help="false" data-raw-max_test_case_length="2048" data-raw-max_test_case_count="10" data-raw-upcoming_downtime="null" data-raw-task_names="[&quot;binary_gap&quot;]" data-raw-task_types="{&quot;binary_gap&quot;: &quot;normal&quot;}" data-raw-task_impacts="{}" data-raw-current_task_name="&quot;binary_gap&quot;" data-raw-time_elapsed_sec="null" data-raw-time_remaining_sec="7200" data-raw-expected_close_date="null" data-raw-has-multi-file-tasks="null" data-raw-should-use-version-submit-flow="true" data-raw-has-weighted-scoring="false" data-raw-ticket-url="&quot;https://app.codility.com/test/trainingR4ZZZF-PJE/&quot;" data-raw-branding-primary-theme-color="null" data-raw-logos="{&quot;has_primary_logo&quot;: true}" data-raw-demo="false" data-raw-cert="false" data-raw-training="true" data-raw-is_codelive="false" data-raw-support_email="&quot;support@codility.com&quot;" data-raw-support_link="null" data-raw-show_test_cases="true" data-raw-accessibility_mode="false" data-raw-enable_beta_testing="false" data-raw-should-enable-autocomplete="false" data-raw-enable_twilio_debug_logs="false" data-raw-enable_interviewer_login="false" data-raw-enable-monaco-editor-for-programmers-home="true" data-raw-enable-monaco-editor-in-code-check="true" data-raw-enable-monaco-with-autocomplete="true" data-raw-features="[{&quot;name&quot;: &quot;AUTOCOMPLETE_IN_CODE_CHECK&quot;}, {&quot;name&quot;: &quot;CAN_EXPORT_PDF&quot;}, {&quot;name&quot;: &quot;SSO_LOGIN_ENABLED&quot;}]" data-raw-id-verification-enabled="false"></div>
  
  <div id="js-candidate-interface"><div id="page" class="Interface__PageWrapper-sc-19ytpcx-1 hsmSwS"><input type="hidden" name="ticket" value="{{ticket.id}}"><div id="header" role="region" class="Interface__TopBarWrapper-sc-19ytpcx-0 hvjsDJ"><div height="42" class="UntypedBox__Wrapper-sc-4e7tnk-0 hjseYc styles__Wrapper-sc-1lsv3fx-0 ftqOyi"><div class="UntypedBox__Wrapper-sc-4e7tnk-0 dyHGhe"><div width="48px" class="UntypedBox__Wrapper-sc-4e7tnk-0 hNsZSR TopBarLogo__CodilityLogoWrapper-sc-kzmwh-1 FWXta"><div class="Logo__Wrapper-sc-zvecf3-0 gcmNyG"><canvas height="95" width="137" class="Logo__AspectRatioHelper-sc-zvecf3-1 iufKsk"></canvas><svg xmlns="http://www.w3.org/2000/svg" width="137" height="95" fill-rule="evenodd" viewBox="0 0 137 95" aria-label="Codility logo graphic" class="Logo__LogoSvg-sc-zvecf3-2 gkPgtp"><path d="M45.867 94.254C20.573 94.254 0 73.122 0 47.142S20.603 0 45.867 0c9.483-.007 18.723 2.996 26.4 8.575.525.386.87.97.957 1.614s-.095 1.3-.502 1.808l-8.038 10.074a2.47 2.47 0 0 1-1.909.917c-.51.003-1.003-.168-1.402-.485a24.61 24.61 0 0 0-15.495-5.578c-14.914 0-27.038 13.788-27.038 30.73S30.953 78.4 45.867 78.4a24.69 24.69 0 0 0 15.95-5.965c.416-.352.946-.54 1.49-.53.76.006 1.475.35 1.954.94l7.457 9.366c.406.51.588 1.162.502 1.808s-.43 1.23-.957 1.614c-7.662 5.6-16.907 8.62-26.397 8.62" fill="#fff"></path><path d="M133.164 65.27H100.1c-.133.006-.265.024-.395.052l-.395-.052c-1.27.007-2.405.8-2.85 1.99l-4.474 12.08a3.04 3.04 0 0 0 2.849 4.094h8.948c.212.055.43.088.65.097h28.724c.803 0 1.572-.323 2.133-.897s.868-1.35.85-2.153V68.32c.018-.8-.287-1.576-.847-2.15s-1.327-.898-2.128-.9z" fill="#ffe400"></path></svg></div></div></div><div class="UntypedBox__Wrapper-sc-4e7tnk-0 Xbyel"><div class="Box__Wrapper-sc-6lvy0r-0 dcSSLL"><div class="Box__Wrapper-sc-6lvy0r-0 hwSyoC TimerDisplay___StyledBox-sc-zio99o-1 ctPAII" height="36" data-test-id="clock" data-help="clock"><svg viewBox="0 0 24 24" class="Icon__IconWrapper-sc-11q5sbx-0 jsVJuZ has-min-height has-min-width" aria-label="timer icon" aria-hidden="true"><path d="M12 7a.834.834 0 00-.833.833V12h-2.5a.834.834 0 000 1.667h4.166V7.833A.834.834 0 0012 7zm0-5C6.478 2 2 6.478 2 12c0 5.523 4.478 10 10 10 5.523 0 10-4.477 10-10 0-5.522-4.477-10-10-10zm0 17.5a7.5 7.5 0 11.001-15.001A7.5 7.5 0 0112 19.5z"></path></svg><p role="timer" aria-live="polite" aria-atomic="true" class="text__P-sc-1rm5cia-1 bpxvAV specificity-increaser text__BasicText-sc-1rm5cia-4 TimerDisplay___StyledBasicText-sc-zio99o-2 hroZOR iDLmPt"><span class="TimerDisplay__TimerLabel-sc-zio99o-0 eqBkTf">Time remaining:&nbsp;</span><span>1<small>h</small> 57<small>min</small></span><span style="display: block; margin-bottom: -2px;"></span></p></div></div></div><div class="UntypedBox__Wrapper-sc-4e7tnk-0 dAmGit TopBar__ButtonBox-sc-1i0bm84-0 hlzRZu"><button class="Button__ButtonWrapper-sc-hbh4t9-0 htfAJU has-min-width" role="button" tabindex="0" id="submit-button" data-test-id="submit-button" type="button"><svg viewBox="0 0 24 24" class="Icon__IconWrapper-sc-11q5sbx-0 jsVJuZ ButtonIcon-sc-1le4o5g-0 eSJKmX has-min-height has-min-width"><path d="M19.424 5.861a1.629 1.629 0 00-2.254.2l-7.079 8.286-3.604-2.343a1.624 1.624 0 00-2.218.433 1.537 1.537 0 00.444 2.164l5.996 3.899 8.92-10.44a1.535 1.535 0 00-.205-2.199z"></path></svg>Submit Task</button></div></div></div><div id="content"><div id="sidebar" style="height: 100%;"><div class="Sidebar-sc-14bvehk-0 kjbLUL"><nav role="navigation"><div role="tablist" data-help="activity-list" data-test-id="activity-list" tabindex="0"><button class="Button__ButtonWrapper-sc-hbh4t9-0 kHXqrf has-min-width SidebarButton__StyledButton-sc-1n8tbhh-0 kNnCKg" role="tab" tabindex="-1" aria-label="Task 1" data-test-id="activity-button" aria-selected="true" type="button" style="width: 48px;"><div class="Box__Wrapper-sc-6lvy0r-0 kSauGj"><p class="text__P-sc-1rm5cia-1 bpxvAV specificity-increaser text__BasicText-sc-1rm5cia-4 bJvLKi">1</p></div></button></div></nav><div class="SidebarSpacer-sc-tskolr-0 kUcTvP"></div><div role="complementary" class="SidebarSection-sc-r7nok7-0 jOsRvX"><div class="Box__Wrapper-sc-6lvy0r-0 cCsnJf"><button class="Button__ButtonWrapper-sc-hbh4t9-0 kHXqrf has-min-width SidebarButton__StyledButton-sc-1n8tbhh-0 hCTqSJ" role="button" tabindex="0" aria-label="Enable accessibility mode" data-test-id="accessibility-btn" id="accessibility_btn" data-accessibility-mode="false" type="button" style="width: 48px;"><div class="Box__Wrapper-sc-6lvy0r-0 kSauGj"><svg viewBox="0 0 24 24" class="Icon__IconWrapper-sc-11q5sbx-0 gfkMVw has-min-height has-min-width"><path d="M12 2C6.478 2 2 6.478 2 12c0 5.523 4.478 10 10 10 5.523 0 10-4.477 10-10 0-5.522-4.477-10-10-10zm0 3.333a1.667 1.667 0 11-.001 3.335A1.667 1.667 0 0112 5.333zM16.583 12H14.5v5.833a.836.836 0 01-.833.834.836.836 0 01-.834-.834v-2.5h-1.666v2.5a.836.836 0 01-.834.834.836.836 0 01-.833-.834V12H7.417a.836.836 0 01-.834-.833c0-.459.375-.834.834-.834h9.166c.459 0 .834.375.834.834a.836.836 0 01-.834.833z"></path></svg></div></button></div><div class="Box__Wrapper-sc-6lvy0r-0 cCsnJf"><button class="Button__ButtonWrapper-sc-hbh4t9-0 kHXqrf has-min-width SidebarButton__StyledButton-sc-1n8tbhh-0 hCTqSJ" role="button" tabindex="0" aria-label="Editor settings" data-test-id="open-settings-btn" id="open_settings_btn" type="button" style="width: 48px;"><div class="Box__Wrapper-sc-6lvy0r-0 kSauGj"><svg viewBox="0 0 24 24" class="Icon__IconWrapper-sc-11q5sbx-0 gfkMVw has-min-height has-min-width"><path d="M20.416 14.048l-1.273-1.09a7.86 7.86 0 00.065-.958 7.86 7.86 0 00-.065-.958l1.273-1.09a1.713 1.713 0 00.369-2.12l-.924-1.664c-.392-.706-1.216-1.014-1.949-.728l-1.549.605a7.16 7.16 0 00-1.59-.966l-.27-1.686C14.374 2.589 13.706 2 12.923 2h-1.846c-.783 0-1.452.59-1.58 1.393l-.27 1.686a7.123 7.123 0 00-1.59.966l-1.55-.605c-.732-.286-1.557.022-1.95.728l-.922 1.664a1.713 1.713 0 00.369 2.12l1.273 1.09a7.86 7.86 0 00-.065.958c0 .325.027.643.065.958l-1.273 1.09a1.713 1.713 0 00-.369 2.12l.924 1.664c.392.706 1.216 1.014 1.949.728l1.549-.605a7.16 7.16 0 001.59.966l.27 1.686c.129.804.797 1.393 1.58 1.393h1.846c.783 0 1.452-.59 1.58-1.393l.27-1.686a7.123 7.123 0 001.59-.966l1.55.605c.732.286 1.557-.022 1.95-.728l.922-1.664a1.712 1.712 0 00-.369-2.12zM12 15.333c-1.808 0-3.273-1.493-3.273-3.334 0-1.84 1.465-3.333 3.273-3.333 1.807 0 3.273 1.492 3.273 3.333 0 1.841-1.466 3.334-3.273 3.334z"></path></svg></div></button></div><div class="Box__Wrapper-sc-6lvy0r-0 cCsnJf"><button class="Button__ButtonWrapper-sc-hbh4t9-0 kHXqrf has-min-width SidebarButton__StyledButton-sc-1n8tbhh-0 hCTqSJ" role="button" tabindex="0" aria-label="Help" data-test-id="help-btn" id="help_btn" type="button" style="width: 48px;"><div class="Box__Wrapper-sc-6lvy0r-0 kSauGj"><svg viewBox="0 0 24 24" class="Icon__IconWrapper-sc-11q5sbx-0 gfkMVw has-min-height has-min-width"><path d="M4.926 4.926c3.901-3.901 10.247-3.901 14.15 0 3.9 3.9 3.9 10.248-.002 14.149A9.972 9.972 0 0112 22a9.972 9.972 0 01-7.074-2.925c-3.901-3.9-3.901-10.248 0-14.149zm6.949 10.564c-.697 0-1.255.538-1.255 1.245a1.25 1.25 0 001.255 1.255c.707 0 1.235-.568 1.245-1.255a1.22 1.22 0 00-1.245-1.245zM11.831 6c-1.31 0-2.32.645-2.926 1.528a.865.865 0 00.397 1.3l.111.037c.373.098.755-.07.98-.395.288-.427.754-.784 1.458-.784 1.607 0 1.925 1.508 1.36 2.312-.537.763-1.459 1.28-1.945 2.142a2.503 2.503 0 00-.298 1.022.87.87 0 00.873.952h.06c.446 0 .843-.327.893-.773.03-.308.089-.447.188-.625.387-.705 1.101-1.052 1.855-2.153.674-1.002.417-2.341-.02-3.055C14.301 6.665 13.3 6 11.831 6z"></path></svg></div></button></div><div class="Box__Wrapper-sc-6lvy0r-0 cCsnJf"><button class="Button__ButtonWrapper-sc-hbh4t9-0 kHXqrf has-min-width SidebarButton__StyledButton-sc-1n8tbhh-0 hCTqSJ" role="button" tabindex="0" aria-label="Exit" data-test-id="quit-btn" id="quit_button" type="button" style="width: 48px;"><div class="Box__Wrapper-sc-6lvy0r-0 kSauGj"><svg viewBox="0 0 24 24" class="Icon__IconWrapper-sc-11q5sbx-0 gfkMVw has-min-height has-min-width"><path d="M11.03 8.03a.75.75 0 00-1.28.53v1.94H4.5a1.5 1.5 0 000 3h5.25v1.94a.75.75 0 001.28.53L15 12l-3.97-3.97zM16.5 3h-3a1.5 1.5 0 000 3h3c.827 0 1.5.673 1.5 1.5v9c0 .827-.673 1.5-1.5 1.5h-3a1.5 1.5 0 000 3h3c2.482 0 4.5-2.018 4.5-4.5v-9C21 5.018 18.982 3 16.5 3z"></path></svg></div></button></div></div></div></div><div data-test-id="task-ui" role="main" class="TaskInterface__FlexiblePanelWrapper-sc-1by0x4p-0 kfQPT"><div class="FlexiblePanel__Container-sc-irkdfy-0 brlep"><div class="FlexiblePanelArea-sc-xrt7fk-0 jyPTa-D" style="flex: 40 40 0px;"><div id="task" class="UntypedBox__Wrapper-sc-4e7tnk-0 guoFBE Floater-sc-vcx7dh-0 khmGRt help-tour-task-description"><div id="task_description" class="Tabs__Wrapper-sc-1wbc56k-0 htgfit LeftColumn__StyledTab-sc-1ldymr9-1 kSEJdi"><div class="Tabs__Head-sc-1wbc56k-1 iBeESM"><div data-test-id="tab" class="Tab__Wrapper-sc-1d03zop-0 iyCzMi"><div class="Tab__NameWrapper-sc-1d03zop-1 icEVbs"><p aria-level="2" role="heading" class="text__P-sc-1rm5cia-1 bpxvAV specificity-increaser text__BasicText-sc-1rm5cia-4 jzDQhN">Task 1</p></div></div><div class="UntypedBox__Wrapper-sc-4e7tnk-0 fesEaE Tabs__WidgetsWrapper-sc-1wbc56k-2 fGJxFp"><div data-help="task-variants-wrapper" class="UntypedBox__Wrapper-sc-4e7tnk-0 ekvrbw"><div id="select-variant-prg_lang" data-test-id="select-root" class="Select__Wrapper-sc-pdwb8d-2 ihPBOJ"><div id="select-variant-prg_lang-label" data-test-id="select-opener-label" style="border: 0px; clip: rect(0px, 0px, 0px, 0px); clip-path: inset(50%); height: 1px; margin: -1px; overflow: hidden; padding: 0px; position: absolute; width: 1px; white-space: nowrap;">Select Programming Language, Python selected</div><div width="150px" data-test-id="select-opener" data-test-value="py" aria-haspopup="listbox" aria-expanded="false" aria-disabled="false" aria-labelledby="select-variant-prg_lang-label" role="button" class="Select__Opener-sc-pdwb8d-0 fmBGLM" tabindex="0"><span data-test-id="selected-option-label" aria-hidden="true" class="text__Span-sc-1rm5cia-0 SorIc specificity-increaser text__BasicText-sc-1rm5cia-4 jzDQhN">Python</span><div class="DropdownArrow-sc-yepg0h-0 xycIk"></div><input type="hidden" value="py"></div><ul data-test-options-for="select-variant-prg_lang" data-test-id="select-ui-options" aria-activedescendant="select-variant-prg_lang-item-py" aria-expanded="false" aria-label="Select Programming Language" role="listbox" tabindex="-1" class="Options__Wrapper-sc-133dice-0 gOCHFM"><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-c" data-test-value="c" aria-selected="false" role="option">C</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-cpp" data-test-value="cpp" aria-selected="false" role="option">C++</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-cpp_20" data-test-value="cpp_20" aria-selected="false" role="option">C++20</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-cs" data-test-value="cs" aria-selected="false" role="option">C#</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-dart" data-test-value="dart" aria-selected="false" role="option">Dart</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-go" data-test-value="go" aria-selected="false" role="option">Go</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-java" data-test-value="java" aria-selected="false" role="option">Java 8</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-java11" data-test-value="java11" aria-selected="false" role="option">Java 11</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-js" data-test-value="js" aria-selected="false" role="option">JavaScript</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-kt" data-test-value="kt" aria-selected="false" role="option">Kotlin</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-lua" data-test-value="lua" aria-selected="false" role="option">Lua</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-m" data-test-value="m" aria-selected="false" role="option">Objective-C</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-pas" data-test-value="pas" aria-selected="false" role="option">Pascal</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-php" data-test-value="php" aria-selected="false" role="option">PHP</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-pl" data-test-value="pl" aria-selected="false" role="option">Perl</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-py" data-test-value="py" aria-selected="false" role="option">Python</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-rb" data-test-value="rb" aria-selected="false" role="option">Ruby</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-scala" data-test-value="scala" aria-selected="false" role="option">Scala</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-ts" data-test-value="ts" aria-selected="false" role="option">TypeScript</li><li class="Option__Wrapper-sc-ajtjk1-0 dxQJFH" id="select-variant-prg_lang-item-vb" data-test-value="vb" aria-selected="false" role="option">Visual Basic</li></ul><fieldset width="150px" class="Select__Fieldset-sc-pdwb8d-4 kpAzYQ"><legend class="Select__Legend-sc-pdwb8d-3 bYFIPK"><p data-test-id="floating-placeholder" class="text__P-sc-1rm5cia-1 bpxvAV specificity-increaser text__SmallSecondaryText-sc-1rm5cia-3 Select__Label-sc-pdwb8d-1 gWskCj bXEvBV">Programming Language</p></legend></fieldset></div></div></div></div><div class="Tabs__Body-sc-1wbc56k-3 eIjwTN"><div class="UntypedBox__Wrapper-sc-4e7tnk-0 gnBbdH Floater-sc-vcx7dh-0 khmGRt TaskDescription__ThemedBox-sc-7m9k5q-0 yJaro"><div class="TaskDescription__ContentContainer-sc-7m9k5q-6 hlglqI"><div id="standard_task_description" class="TaskDescription__StandardTaskDescription-sc-7m9k5q-3 crhSKM standard-task-description"><h2 class="mod-hidden">Task description</h2><div class="TaskDescription__TaskContentWrapper-sc-7m9k5q-2 kDUwpJ task-description-content">




<div class="brinza-task-description">
<p>A <i>binary gap</i> within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.</p>
<p>For example, number 9 has binary representation <tt style="white-space:pre-wrap">1001</tt> and contains a binary gap of length 2. The number 529 has binary representation <tt style="white-space:pre-wrap">1000010001</tt> and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation <tt style="white-space:pre-wrap">10100</tt> and contains one binary gap of length 1. The number 15 has binary representation <tt style="white-space:pre-wrap">1111</tt> and has no binary gaps. The number 32 has binary representation <tt style="white-space:pre-wrap">100000</tt> and has no binary gaps.</p>
<p>Write a function:</p>
<blockquote><p style="font-family: monospace; font-size: 9pt; display: block; white-space: pre-wrap"><tt>def solution(N)</tt></p></blockquote>
<p>that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.</p>
<p>For example, given N = 1041 the function should return 5, because N has binary representation <tt style="white-space:pre-wrap">10000010001</tt> and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.</p>
<p>Write an <b><b>efficient</b></b> algorithm for the following assumptions:</p>
<blockquote><ul style="margin: 10px;padding: 0px;"><li>N is an integer within the range [<span class="number">1</span>..<span class="number">2,147,483,647</span>].</li>
</ul>
</blockquote></div>
<div style="margin-top:5px">
<small>Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.</small>
</div>

</div></div></div></div></div></div><div id="test_cases_area" class="UntypedBox__Wrapper-sc-4e7tnk-0 ekvrbw"></div></div></div><div class="FlexiblePanelDivider__FlexibleLine-sc-1iyq0wt-2 kJxwHk"><div class="FlexiblePanelDivider__FlexiblePanelSubLine-sc-1iyq0wt-0 krquXz"></div><svg viewBox="0 0 48 48" class="Icon__IconWrapper-sc-11q5sbx-0 ElmDp FlexiblePanelDivider__FlexiblePanelIcon-sc-1iyq0wt-1 cgFvUp"><path d="M40 18H8v4h32v-4zM8 30h32v-4H8v4z"></path></svg><div class="FlexiblePanelDivider__FlexiblePanelSubLine-sc-1iyq0wt-0 krquXz"></div></div><div class="FlexiblePanelArea-sc-xrt7fk-0 jyPTa-D" style="flex: 60 60 0px;"><div style="height: 100%;"><div class="RightColumn__RightColumnWrapper-sc-km4mib-1 iVHRUK"><div id="rightColumn"><div id="rightEditorAndTestOutput" class="RightColumn__EditorAndTestOutput-sc-km4mib-0 jFYVap"><div id="edit"><div id="solution_wrapper"><h2 class="mod-hidden">Solution</h2><div id="working-area-container"><div class="FlexiblePanel__Container-sc-irkdfy-0 eJthNx"><div class="FlexiblePanelArea-sc-xrt7fk-0 jjtAZf help-tour-editor" style="flex: 66.6667 66.6667 0px;"><div class="Box__Wrapper-sc-6lvy0r-0 hNcWz" height="100%" id="working-area-editor"><div class="FlexiblePanel__Container-sc-irkdfy-0 brlep"><div class="FlexiblePanelArea-sc-xrt7fk-0 jdUrBt" style="flex: 0 0 0px;"><div data-help="task-files-tree" data-test-id="task-files-tree" class="Tabs__Wrapper-sc-1wbc56k-0 htgfit Tabs__FloatingTabs-sc-1wbc56k-4 SolutionFilesTree__StyledFloatingTab-sc-klcfbg-1 eGdmh juKaXo"><div class="Tabs__Head-sc-1wbc56k-1 iBeESM"><div data-test-id="tab" class="Tab__Wrapper-sc-1d03zop-0 iyCzMi"><div class="Tab__NameWrapper-sc-1d03zop-1 icEVbs"><span role="heading" aria-level="2">Files</span></div></div></div><div class="Tabs__Body-sc-1wbc56k-3 eIjwTN"><div height="100%" class="UntypedBox__Wrapper-sc-4e7tnk-0 gZSUTW SolutionFilesTree__TreeWrapperBox-sc-klcfbg-0 hZtpEU"><div id="FileTree" role="tree" tabindex="0" aria-label="File tree" class="Tree__TreeWrapper-sc-ff9037-0 isVPzJ"><div role="treeitem" aria-level="1" aria-selected="false" data-focus-id="tree-node-FileTreetask1" data-test-id="tree-root" data-help="tree-node" id="dropdown-auto-id-4" class="UntypedBox__Wrapper-sc-4e7tnk-0 cHJhCa TreeNodeWrapper__Wrapper-sc-1ev5co-0 jkIDnZ" aria-label="task1" aria-expanded="true" tabindex="-1"><div class="Box__Wrapper-sc-6lvy0r-0 gGfVBs TreeNodeLabel__LabelWrapper-sc-1vqy96p-1 bkRGss" aria-hidden="true" data-test-label="task1"><svg viewBox="0 0 24 24" class="Icon__IconWrapper-sc-11q5sbx-0 erPgKd TreeNodeIcon__OpenFolderIcon-sc-13xqevv-3 keuTK has-min-height has-min-width"><path d="M6.564 8.95h12.103v-.825c0-.91-.747-1.65-1.667-1.65h-5.833L9.5 4H3.667C2.747 4 2 4.74 2 5.65v9.632l1.39-4.128C3.833 9.835 5.11 8.95 6.564 8.95zm13.769 1.65H6.565c-.732 0-1.377.436-1.592 1.075L2 20.5h16.667l3.258-7.93c.33-.978-.472-1.97-1.592-1.97z"></path></svg><p title="task1" class="text__P-sc-1rm5cia-1 bpxvAV specificity-increaser text__BasicText-sc-1rm5cia-4 TreeNodeLabel__Label-sc-1vqy96p-0 jzDQhN hpMrTT">task1</p></div></div><div role="treeitem" aria-level="2" aria-selected="true" data-focus-id="tree-node-FileTreesolution.py" data-test-id="tree-node-solution.py" data-help="tree-node" id="dropdown-auto-id-5" class="UntypedBox__Wrapper-sc-4e7tnk-0 cHJhCa TreeNodeWrapper__Wrapper-sc-1ev5co-0 kkHJJy" aria-label="solution.py" tabindex="-1"><div class="Box__Wrapper-sc-6lvy0r-0 MxeIw TreeNodeLabel__LabelWrapper-sc-1vqy96p-1 fZwzjK" aria-hidden="true" data-test-label="solution.py"><svg viewBox="0 0 24 24" class="Icon__IconWrapper-sc-11q5sbx-0 erPgKd TreeNodeIcon__FileIcon-sc-13xqevv-4 bSIFlF has-min-height has-min-width"><path d="M15 3v4.5h4.5L15 3zm-1.5 0H6a1.5 1.5 0 00-1.5 1.5v15A1.5 1.5 0 006 21h12a1.5 1.5 0 001.5-1.5V9h-6V3z"></path></svg><p title="solution.py" class="text__P-sc-1rm5cia-1 bpxvAV specificity-increaser text__BasicText-sc-1rm5cia-4 TreeNodeLabel__Label-sc-1vqy96p-0 jzDQhN hpMrTT">solution.py</p></div></div><div role="treeitem" aria-level="2" aria-selected="false" data-focus-id="tree-node-FileTreetest-input.txt" data-test-id="tree-node-test-input.txt" data-help="tree-node" id="dropdown-auto-id-6" class="UntypedBox__Wrapper-sc-4e7tnk-0 cHJhCa TreeNodeWrapper__Wrapper-sc-1ev5co-0 jkIDnZ" aria-label="test-input.txt" tabindex="-1"><div class="Box__Wrapper-sc-6lvy0r-0 MxeIw TreeNodeLabel__LabelWrapper-sc-1vqy96p-1 fZwzjK" aria-hidden="true" data-test-label="test-input.txt"><svg viewBox="0 0 24 24" class="Icon__IconWrapper-sc-11q5sbx-0 erPgKd TreeNodeIcon__FileIcon-sc-13xqevv-4 bSIFlF has-min-height has-min-width"><path d="M15 3v4.5h4.5L15 3zm-1.5 0H6a1.5 1.5 0 00-1.5 1.5v15A1.5 1.5 0 006 21h12a1.5 1.5 0 001.5-1.5V9h-6V3z"></path></svg><p title="test-input.txt" class="text__P-sc-1rm5cia-1 bpxvAV specificity-increaser text__BasicText-sc-1rm5cia-4 TreeNodeLabel__Label-sc-1vqy96p-0 jzDQhN hpMrTT">test-input.txt</p></div></div></div></div></div></div></div><div class="FlexiblePanelDivider__FlexibleLine-sc-1iyq0wt-2 iwrkX"><div class="FlexiblePanelDivider__FlexiblePanelSubLine-sc-1iyq0wt-0 krquXz"></div><svg viewBox="0 0 48 48" class="Icon__IconWrapper-sc-11q5sbx-0 ElmDp FlexiblePanelDivider__FlexiblePanelIcon-sc-1iyq0wt-1 cgFvUp"><path d="M40 18H8v4h32v-4zM8 30h32v-4H8v4z"></path></svg><div class="FlexiblePanelDivider__FlexiblePanelSubLine-sc-1iyq0wt-0 krquXz"></div></div><div class="FlexiblePanelArea-sc-xrt7fk-0 fNSJMp" style="flex: 100 100 0px;"><div data-test-id="file-tabs-header"><div data-help="solution-editor" class="Tabs__Wrapper-sc-1wbc56k-0 htgfit Tabs__FloatingTabs-sc-1wbc56k-4 FileTabs__StyledFloatingTab-sc-665hip-0 eGdmh kKIMer"><div class="Tabs__Head-sc-1wbc56k-1 iBeESM"><div data-test-id="tab" class="Tab__Wrapper-sc-1d03zop-0 kEmsnK"><div class="Tab__NameWrapper-sc-1d03zop-1 icEVbs"><div data-test-id="tab-title" class="UntypedBox__Wrapper-sc-4e7tnk-0 cxa-DRl"><svg viewBox="0 0 24 24" class="Icon__IconWrapper-sc-11q5sbx-0 ElmDp" alt="file icon" aria-hidden="true"><path d="M15 3v4.5h4.5L15 3zm-1.5 0H6a1.5 1.5 0 00-1.5 1.5v15A1.5 1.5 0 006 21h12a1.5 1.5 0 001.5-1.5V9h-6V3z"></path></svg><div>solution.py</div><svg viewBox="0 0 24 24" class="Icon__IconWrapper-sc-11q5sbx-0 ElmDp" alt="close file icon" aria-label="close file solution.py" tabindex="0" role="button" data-test-id="close-file-icon"><path d="M15.394 6.343L12 9.737 8.606 6.343a1.6 1.6 0 00-2.263 2.263L9.737 12l-3.394 3.394a1.6 1.6 0 002.263 2.263L12 14.263l3.394 3.394a1.6 1.6 0 002.263-2.263L14.263 12l3.394-3.394a1.6 1.6 0 00-2.263-2.263z"></path></svg></div></div></div><div class="UntypedBox__Wrapper-sc-4e7tnk-0 fesEaE Tabs__WidgetsWrapper-sc-1wbc56k-2 fGJxFp"></div></div><div class="Tabs__Body-sc-1wbc56k-3 eIjwTN"><div data-public="true" id="editor" class="Floater-sc-vcx7dh-0 khmGRt"><div class="InternalMonacoEditor__EditorWrapper-sc-1nsgfz-0 InternalMonacoEditor__EditorContainer-sc-1nsgfz-1 ksXVrN iKrAlW"><div data-test-id="monaco-editor" class="InternalMonacoEditor__EditorWrapper-sc-1nsgfz-0 ksXVrN" data-keybinding-context="2" data-mode-id="python" style="--codelens-font-features_ee1f62: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory:solution.py" style="width: 713px; height: 332px;"><div data-mprt="3" class="overflow-guard" style="width: 713px; height: 332px;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: -19px; height: 456px; width: 64px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 456px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; width: 64px; font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; height: 456px;"><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">5</div></div><div style="position:absolute;top:95px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">6</div></div><div style="position:absolute;top:114px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">7</div></div><div style="position:absolute;top:133px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">8</div></div><div style="position:absolute;top:152px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">9</div></div><div style="position:absolute;top:171px;width:100%;height:19px;"><div class="cldr codicon codicon-folding-expanded" style="left:38px;width:26px;"></div><div class="line-numbers" style="left:0px;width:38px;">10</div></div><div style="position:absolute;top:190px;width:100%;height:19px;"><div class="cldr codicon codicon-folding-expanded" style="left:38px;width:26px;"></div><div class="line-numbers" style="left:0px;width:38px;">11</div></div><div style="position:absolute;top:209px;width:100%;height:19px;"><div class="cldr codicon codicon-folding-expanded" style="left:38px;width:26px;"></div><div class="line-numbers" style="left:0px;width:38px;">12</div></div><div style="position:absolute;top:228px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">13</div></div><div style="position:absolute;top:247px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">14</div></div><div style="position:absolute;top:266px;width:100%;height:19px;"><div class="cldr codicon codicon-folding-expanded" style="left:38px;width:26px;"></div><div class="line-numbers" style="left:0px;width:38px;">15</div></div><div style="position:absolute;top:285px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">16</div></div><div style="position:absolute;top:304px;width:100%;height:19px;"><div class="cldr codicon codicon-folding-expanded" style="left:38px;width:26px;"></div><div class="line-numbers" style="left:0px;width:38px;">17</div></div><div style="position:absolute;top:323px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">18</div></div><div style="position:absolute;top:342px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">19</div></div><div style="position:absolute;top:57px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:64px; height:19px;"></div><div class="cldr codicon codicon-folding-expanded" style="left:38px;width:26px;"></div><div class="active-line-number line-numbers" style="left:0px;width:38px;">4</div></div><div style="position:absolute;top:38px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">3</div></div><div style="position:absolute;top:19px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:38px;">2</div></div></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 64px; width: 649px; height: 332px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 1e+06px; transform: translate3d(0px, 0px, 0px); contain: strict; top: -19px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; height: 0px; width: 649px;"><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="core-guide core-guide-indent-active" style="left:0px;height:19px;width:7.69921875px"></div></div><div style="position:absolute;top:95px;width:100%;height:19px;"><div class="core-guide core-guide-indent-active" style="left:0px;height:19px;width:7.69921875px"></div></div><div style="position: absolute; top: 114px; width: 100%; height: 19px;"><div class="core-guide core-guide-indent-active" style="left:0px;height:19px;width:7.69921875px"></div></div><div style="position: absolute; top: 133px; width: 100%; height: 19px;"><div class="core-guide core-guide-indent-active" style="left:0px;height:19px;width:7.69921875px"></div></div><div style="position: absolute; top: 152px; width: 100%; height: 19px;"><div class="core-guide core-guide-indent-active" style="left:0px;height:19px;width:7.69921875px"></div></div><div style="position: absolute; top: 171px; width: 100%; height: 19px;"><div class="core-guide core-guide-indent-active" style="left:0px;height:19px;width:7.69921875px"></div></div><div style="position: absolute; top: 190px; width: 100%; height: 19px;"><div class="core-guide core-guide-indent-active" style="left:0px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:30.796875px;height:19px;width:7.69921875px"></div></div><div style="position: absolute; top: 209px; width: 100%; height: 19px;"><div class="core-guide core-guide-indent-active" style="left:0px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:30.796875px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:61.59375px;height:19px;width:7.69921875px"></div></div><div style="position: absolute; top: 228px; width: 100%; height: 19px;"><div class="core-guide core-guide-indent-active" style="left:0px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:30.796875px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:61.59375px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:92.390625px;height:19px;width:7.69921875px"></div></div><div style="position: absolute; top: 247px; width: 100%; height: 19px;"><div class="core-guide core-guide-indent-active" style="left:0px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:30.796875px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:61.59375px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:92.390625px;height:19px;width:7.69921875px"></div></div><div style="position: absolute; top: 266px; width: 100%; height: 19px;"><div class="core-guide core-guide-indent-active" style="left:0px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:30.796875px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:61.59375px;height:19px;width:7.69921875px"></div></div><div style="position: absolute; top: 285px; width: 100%; height: 19px;"><div class="core-guide core-guide-indent-active" style="left:0px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:30.796875px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:61.59375px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:92.390625px;height:19px;width:7.69921875px"></div></div><div style="position: absolute; top: 304px; width: 100%; height: 19px;"><div class="core-guide core-guide-indent-active" style="left:0px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:30.796875px;height:19px;width:7.69921875px"></div></div><div style="position: absolute; top: 323px; width: 100%; height: 19px;"><div class="core-guide core-guide-indent-active" style="left:0px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:30.796875px;height:19px;width:7.69921875px"></div><div class="core-guide core-guide-indent" style="left:61.59375px;height:19px;width:7.69921875px"></div></div><div style="position: absolute; top: 342px; width: 100%; height: 19px;"><div class="core-guide core-guide-indent-active" style="left:0px;height:19px;width:7.69921875px"></div></div><div style="position:absolute;top:57px;width:100%;height:19px;"><div class="current-line" style="width:649px; height:19px;"></div></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; width: 649px; height: 456px;"><div style="top: 76px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;binary&nbsp;=&nbsp;</span><span class="mtk11">bin</span><span class="mtk1">(N)[</span><span class="mtk7">2</span><span class="mtk1">:]&nbsp;</span></span></div><div style="top: 95px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;max_gap&nbsp;=&nbsp;</span><span class="mtk7">0</span></span></div><div style="top: 114px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;current_gap&nbsp;=&nbsp;</span><span class="mtk7">0</span></span></div><div style="top: 133px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;counting&nbsp;=&nbsp;</span><span class="mtk4">False</span></span></div><div style="top: 152px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 171px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk13">for</span><span class="mtk1">&nbsp;digit&nbsp;</span><span class="mtk13">in</span><span class="mtk1">&nbsp;binary:</span></span></div><div style="top: 190px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk13">if</span><span class="mtk1">&nbsp;digit&nbsp;==&nbsp;</span><span class="mtk8">'1'</span><span class="mtk1">:</span></span></div><div style="top: 209px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk13">if</span><span class="mtk1">&nbsp;counting:</span></span></div><div style="top: 228px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_gap&nbsp;=&nbsp;</span><span class="mtk11">max</span><span class="mtk1">(max_gap,&nbsp;current_gap)</span></span></div><div style="top: 247px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;current_gap&nbsp;=&nbsp;</span><span class="mtk7">0</span></span></div><div style="top: 266px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk13">else</span><span class="mtk1">:</span></span></div><div style="top: 285px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;counting&nbsp;=&nbsp;</span><span class="mtk4">True</span></span></div><div style="top: 304px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk13">elif</span><span class="mtk1">&nbsp;counting:</span></span></div><div style="top: 323px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;current_gap&nbsp;+=&nbsp;</span><span class="mtk7">1</span></span></div><div style="top: 342px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk4">def</span><span class="mtk1">&nbsp;</span><span class="mtk11">solution</span><span class="mtk1">(</span><span class="mtk14">N</span><span class="mtk1">):</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk3">#&nbsp;print("this&nbsp;is&nbsp;a&nbsp;debug&nbsp;message")</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="codicon-light-bulb codicon" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; visibility: hidden; max-width: 649px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 57px; left: 123px; font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 635px; height: 12px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 12px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 635px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="415" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 332px;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical fade" style="position: absolute; width: 14px; height: 332px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 14px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 241px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 713px;" class="scroll-decoration"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="off" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; top: 38px; left: 187px; width: 1px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 713px;"><div class="accessibilityHelpWidget" role="dialog" aria-hidden="true" widgetid="editor.contrib.accessibilityHelpWidget" style="display: none; position: absolute;"><div role="document"></div></div><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 332px;"><div class="minimap-shadow-hidden" style="height: 332px;"></div><canvas width="0" height="415" style="position: absolute; left: 0px; width: 0px; height: 332px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="415" style="position: absolute; left: 0px; width: 0px; height: 332px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div></div><div data-mprt="2" class="overflowingContentWidgets"><div class="monaco-editor rename-box" widgetid="__renameInputWidget" style="background-color: rgb(37, 37, 38); box-shadow: rgba(0, 0, 0, 0.36) 0px 0px 8px 2px; color: rgb(204, 204, 204); position: fixed; visibility: hidden; max-width: 1536px;"><input class="rename-input" type="text" aria-label="Rename input. Type new name and press Enter to commit." style="font-family: Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; background-color: rgb(60, 60, 60); border-width: 0px; border-style: none;"><div class="rename-label" style="font-size: 11.2px;">Enter to Rename, Shift+Enter to Preview</div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip" widgetid="editor.contrib.modesContentHoverWidget" style="position: fixed; visibility: hidden; max-width: 1536px; top: 191.8px; left: 918.237px;"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 19px; max-height: 250px; max-width: 500px;"><div class="hover-row markdown-hover"><div class="hover-contents"><div><p>int(x=0) -&gt; integer
int(x, base=10) -&gt; integer</p><p>Convert a number or string to an integer, or return 0 if no arguments
are given.&nbsp;&nbsp;If x is a number, return x.<strong>int</strong>().&nbsp;&nbsp;For floating point
numbers, this truncates towards zero.</p><p>If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.&nbsp;&nbsp;The literal can be preceded by '+' or '-' and be surrounded
by whitespace.&nbsp;&nbsp;The base defaults to 10.&nbsp;&nbsp;Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.</p><blockquote>
<blockquote>
<blockquote>
<p>int('0b100', base=0)
4</p></blockquote>
</blockquote>
</blockquote>
</div></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 490px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 490px;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 10px; height: 236px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 236px;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div><div class="context-view" aria-hidden="true" style="display: none;"></div></div></div><div tabindex="0" class="EditorHint__HintWrapper-sc-1s8u3p8-0 lcZslL"><p class="text__P-sc-1rm5cia-1 bpxvAV specificity-increaser text__SmallText-sc-1rm5cia-2 aRQKM">To leave editor use Ctrl + M</p><p class="text__P-sc-1rm5cia-1 bpxvAV specificity-increaser text__SmallText-sc-1rm5cia-2 aRQKM">Language Version: Python 3.8.10</p></div></div></div></div></div></div></div></div></div></div><div class="FlexiblePanelDivider__FlexibleLine-sc-1iyq0wt-2 jTkazn"><div class="FlexiblePanelDivider__FlexiblePanelSubLine-sc-1iyq0wt-0 hMuFQv"></div><svg viewBox="0 0 48 48" class="Icon__IconWrapper-sc-11q5sbx-0 ElmDp FlexiblePanelDivider__FlexiblePanelIcon-sc-1iyq0wt-1 cgFvUp"><path d="M40 18H8v4h32v-4zM8 30h32v-4H8v4z"></path></svg><div class="FlexiblePanelDivider__FlexiblePanelSubLine-sc-1iyq0wt-0 hMuFQv"></div></div><div class="FlexiblePanelArea-sc-xrt7fk-0 exRFoq" style="flex: 33.3333 33.3333 0px;"><div class="UntypedBox__Wrapper-sc-4e7tnk-0 guoFBE Floater-sc-vcx7dh-0 khmGRt"><div class="Tabs__Wrapper-sc-1wbc56k-0 htgfit"><div class="Tabs__Head-sc-1wbc56k-1 iBeESM"><div data-test-id="tab" aria-live="polite" aria-atomic="true" class="Tab__Wrapper-sc-1d03zop-0 kACtym"><div class="Tab__NameWrapper-sc-1d03zop-1 icEVbs"><span role="heading" aria-level="2">Test Output</span></div><div class="Box__Wrapper-sc-6lvy0r-0 cCsnJf"><div role="tooltip" data-test-id="tab-status" data-test-status="success" aria-label="Example tests passed" tabindex="0" class="TabStatus__IconWrapper-sc-12fcwfg-0 eVCGYa"><svg viewBox="0 0 14 14" color="brandGreen" class="statuses__Wrapper-sc-qlcqi6-0 KFDOd"><path d="M 7,0 C 3.13,0 0,3.13 0,7 c 0,3.87 3.13,7 7,7 3.87,0 7,-3.13 7,-7 C 14,3.13 10.87,0 7,0 Z M 6,11 2,7.5 3,6 6,8.5 10.5,4 11.5,5.5 6,11 Z"></path></svg></div></div></div><div class="UntypedBox__Wrapper-sc-4e7tnk-0 fesEaE Tabs__WidgetsWrapper-sc-1wbc56k-2 fGJxFp"><button class="Button__ButtonWrapper-sc-hbh4t9-0 htfAJU has-min-width" role="button" tabindex="0" id="run-button" data-test-id="run-button" type="button"><svg viewBox="0 0 24 24" class="Icon__IconWrapper-sc-11q5sbx-0 jsVJuZ ButtonIcon-sc-1le4o5g-0 eSJKmX has-min-height has-min-width"><path d="M17.927 10.88l-7.635-5.597C9.348 4.59 8 5.249 8 6.403v11.194c0 1.154 1.348 1.812 2.292 1.12l7.635-5.596c.764-.561.764-1.681 0-2.241z"></path></svg>Run Code</button></div></div><div data-help="output-window" class="Tabs__Body-sc-1wbc56k-3 eIjwTN"><div class="dark-theme" tabindex="0"><p class="TestOutput__A11yHeading-sc-1v41qo8-0 fNAmRb">Test Output</p><div id="cui_test_output" class="Floater-sc-vcx7dh-0 TestOutput__Wrapper-sc-1v41qo8-1 khmGRt byeemL"><br><div class="TestOutputMessage__Wrapper-sc-14xlikr-0 juJJGJ"><div>

<style>
  .verify .success { color: #000; }
  .dark-theme .verify .success { color: #FFF; }

  
  .verify .success.compile-success { color: #058636; }
  .dark-theme .verify .success.compile-success { color: #0a0; }

  .verify .error { color: #e90000; }
  .verify .note {
    font-style: italic;
  }
  .verify .code {
    font-weight: normal;
    color: #737373;
    white-space: pre-wrap;
  }
  .dark-theme .verify .code {
    color: #9e9e9e;
  }
  .verify .comment {
    white-space: pre-wrap;
  }
  .verify .section {
    padding-left: 0.5em;
    margin-left: 0.5em;
    border-left: solid 3px black;
  }
  .verify .section.has-success { border-left-color: #000; }
  .dark-theme .verify .section.has-success { border-left-color: #FFF; }

  .verify .section.has-success.has-compile-success { border-left-color: #058636; }
  .verify .section.has-error { border-left-color: #e90000; }

  .dark-theme .section.has-success.has-compile-success { border-left-color: #0a0; }
</style>

<div class="verify">
  <div class="section has-success has-compile-success">
    
      <div class="success compile-success" aria-label="Compiled successfully" role="status">Compilation successful.</div>
      
    
  </div>
  
    <br>
    
      <div class="section has-success">
    
      
        
        <span class="title">Example test:&nbsp;&nbsp;</span>
        <span class="code">1041</span>
      
      <br>

      
      

      

        
        
          
            <span class="success">OK</span>
          
        
        
        <br>
      
    </div><!-- .section -->
  
    <br>
    
      <div class="section has-success">
    
      
        
        <span class="title">Example test:&nbsp;&nbsp;</span>
        <span class="code">15</span>
      
      <br>

      
      

      

        
        
          
            <span class="success">OK</span>
          
        
        
        <br>
      
    </div><!-- .section -->
  
    <br>
    
      <div class="section has-success">
    
      
        
        <span class="title">Example test:&nbsp;&nbsp;</span>
        <span class="code">32</span>
      
      <br>

      
      

      

        
        
          
            <span class="success">OK</span>
          
        
        
        <br>
      
    </div><!-- .section -->
  
  <br>

  
    
      
        <div class="title summary success">
          Your code is syntactically correct and works properly on the example test.
        </div>
      
      
        <div class="note">
          Note that the example tests are not part of your score. On submission at least 8 test cases not shown here will assess your solution.
        </div>
      
    

  
</div>
</div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div><div class="BottomStatusBar__BottomStatusBarContainer-sc-1hgo7e2-2 jBBBOE"><div class="BottomStatusBar__StatusComponents-sc-1hgo7e2-0 kAONbK"><p class="text__P-sc-1rm5cia-1 bpxvAV specificity-increaser text__SmallText-sc-1rm5cia-2 StatusBarSmallText-sc-svzltb-0 aRQKM kYHLXX">Autocomplete is connected</p><div class="StatusSpacer__Wrapper-sc-k6ffgi-0 eTXnBQ"><p class="text__P-sc-1rm5cia-1 bpxvAV specificity-increaser text__SmallText-sc-1rm5cia-2 StatusBarSmallText-sc-svzltb-0 aRQKM kYHLXX">|</p></div><p data-help="editor-status-bar" data-test-id="editor-status-bar" class="text__P-sc-1rm5cia-1 bpxvAV specificity-increaser text__SmallText-sc-1rm5cia-2 StatusBarSmallText-sc-svzltb-0 aRQKM kYHLXX">All changes saved</p></div><div class="BottomStatusBar__ControlComponents-sc-1hgo7e2-1 fkNxGk"><div class="ReportIssueButton__Wrapper-sc-11ypp9u-0 iGjhKJ"><button aria-label="Give Feedback" class="ReportIssueButton__ButtonWrapper-sc-11ypp9u-1 fTFIBA"><p class="text__P-sc-1rm5cia-1 bpxvAV specificity-increaser text__SmallText-sc-1rm5cia-2 StatusBarSmallText-sc-svzltb-0 aRQKM hJFSbm">Give Feedback</p><svg viewBox="0 0 24 24" class="Icon__IconWrapper-sc-11q5sbx-0 OYxOE ReportIssueButton__IconWithMargin-sc-11ypp9u-2 YbTUh has-min-height has-min-width"><path d="M19.7,5.3H8.3v9.3h11.3L17,10L19.7,5.3z M6,4C5.4,4,5,4.4,5,5v14c0,0.5,0.4,1,1,1s1-0.5,1-1V5C7,4.4,6.6,4,6,4z"></path></svg></button></div></div></div><div id="downtime_modal_container"></div><div><div id="upload_progress" class="jqmWindow jqm-init" style="display: none;"><div class="message" tabindex="0">?</div><div id="up_loader"><div class="ui progress"><div class="bar"></div><div class="label"></div></div></div></div><div id="modal_editor" class="jqmWindow jqm-init" style="display: none;"><h2>Your test case</h2><div class="warnings"></div><div class="params"></div><div class="dialog_buttons"><input type="button" class="ok" value="OK"><input type="button" class="cancel" value="Cancel"><input type="button" class="undo" value="Undo"></div></div></div></div><div><div role="log" aria-live="assertive" style="border: 0px; clip: rect(0px, 0px, 0px, 0px); height: 1px; margin: -1px; overflow: hidden; white-space: nowrap; padding: 0px; width: 1px; position: absolute;"></div><div role="log" aria-live="assertive" style="border: 0px; clip: rect(0px, 0px, 0px, 0px); height: 1px; margin: -1px; overflow: hidden; white-space: nowrap; padding: 0px; width: 1px; position: absolute;"></div><div role="log" aria-live="polite" style="border: 0px; clip: rect(0px, 0px, 0px, 0px); height: 1px; margin: -1px; overflow: hidden; white-space: nowrap; padding: 0px; width: 1px; position: absolute;"></div><div role="log" aria-live="polite" style="border: 0px; clip: rect(0px, 0px, 0px, 0px); height: 1px; margin: -1px; overflow: hidden; white-space: nowrap; padding: 0px; width: 1px; position: absolute;"></div></div></div>

  
  



<div data-test-id="auto-id-0"><div class="Notifications__Wrapper-sc-1mf19wd-0 hoDayX"></div></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div></body></html>