import re
text = ```
<!doctype html>
<!--[if IE 8]>         <html class="ie8"> <![endif]-->
<!--[if IE 9]>         <html class="ie9"> <![endif]-->
<html class="is-modern" lang="en">
  <head>
    <meta charset="utf-8">

    <title>Validation Errors | All | Java - Braintree Developer Documentation</title>

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <meta name="google-site-verification" content="vFON0Wga-luQ_6VzKxCNLqFMYb49GWhusn2yncPzvuA" />
    

    <!-- Do not move this any further down the head. This snippet needs to load as early as possible. -->
      <script src="https://cdn.optimizely.com/js/6388910444.js"></script>
    <link rel="stylesheet" href="/css/app.css?4735cf8cfa73c7de6513366cef0034697f6014ee">
    <script src="/js/vendor/modernizr.js?4735cf8cfa73c7de6513366cef0034697f6014ee"></script>

    <!--[if lt IE 10]>
    <script src="/js/vendor/fallback/es5-shim.min.js"></script>
    <script src="/js/vendor/fallback/es5-sham.min.js"></script>
    <script src="/js/lib/fallbacks.js"></script>
    <![endif]-->
      <link href="/img/favicon.ico?4735cf8cfa73c7de6513366cef0034697f6014ee" rel="shortcut icon" type="image/x-icon" />
    <link type="text/css" rel="stylesheet" href="//fast.fonts.net/cssapi/f750d5c7-baa2-4767-afd7-45484f47fe17.css"/>

  </head>
  <body class="developers-site">
  <div class="root ">
    <div class="flex app">
        <header class="header">
          <a class="logo" href="/">
            <h1 class="logo--fallback">Braintree_developers</h1>
            <div class="logo--mark"></div>
          </a>
          <div class="header__nav">
            <ul class="nav__list" id="main-nav-links">
                  <li class="nav__item">
                    <a class="nav__link " href="/start" data-autotrack="dd__navbar--get-started" data-track-event-properties="project=journey,action=click,type=link,container=header,descriptor=get started,origin=b_docs">Get Started</a>
                  </li>
                  <li class="nav__item">
                    <a class="nav__link " href="/guides" data-autotrack="dd__navbar--guides" data-track-event-properties="project=journey,action=click,type=link,container=header,descriptor=guides,origin=b_docs">Guides</a>
                  </li>
                  <li class="nav__item">
                    <a class="nav__link is-active" href="/reference" data-autotrack="dd__navbar--reference"d ata-track-event-properties="project=journey,action=click,type=link,container=header,descriptor=reference,origin=b_docs">Reference</a>
                  </li>
            </ul>
          </div>
            <div class="header__search">
              <div class="search" id="nav_search_bar">
                <div class="search__panels">
                  <div class="search__panel search__panel--primary">
                    <div class="search__input-group">
                      <svg viewBox="0 0 24 24"  class="icon--svg search__icon search__icon--search" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
                        <title>Search magnifying glass</title>
                        <path d="M14.8,13.3A6.71,6.71,0,0,0,16,9.5,6.5,6.5,0,1,0,9.5,16a6.71,6.71,0,0,0,3.8-1.2L19,20.49,20.49,19ZM9.5,14A4.5,4.5,0,1,1,14,9.5,4.49,4.49,0,0,1,9.5,14Z"/>
                        <path fill="none" d="M0,0H24V24H0Z"/>
                        <image class="icon--fallback" xlink:href="" src="/img/fallback/icon--search-glass.png">
                      </svg>
                      <input aria-label="Search docs" type="text" placeholder="Search Docs" class="search__input js-search-input" data-track-event-properties="project=journey,action=click,type=search,descriptor=focus search bar,origin=b_docs" />
                      <p class="search__keyboard-shortcut">Type <span>S</span> to search</p>
                    </div>
                    <div class="hits-container hits-container--primary">
                        <div class="hits-container__header isHidden">
                          <h2 class="hits-container__title">Developer Docs</h2>
                            <div class="search__filter" aria-label="Filter results" tabIndex="0">
                              <div class="search__filter-reset"></div>
                              <div class="search__filter-refinement"></div>
                            </div>
                        </div>
                        <div class="hits--primary">
                          <div class="hits-container__placeholder">Start typing to search</div>
                        </div>
                      </div>
                  </div>
                  <div class="search__panel search__panel--secondary">
                    <div class="hits-container hits-container--secondary">
                      <div class="hits-container__header isHidden">
                        <h2 class="hits-container__title">Support Articles</h2>
                          <div class="search__tooltip">
                            <button class="search__button--tooltip" aria-label="what are support articles?">
                              <svg id="tooltip" viewBox="0 0 20 20" class="icon--svg search__icon search__icon--tooltip" aria-labeledby="information-tooltip" xmlns="http://www.w3.org/2000/svg">
                                <title id="information-tooltip">Informational tooltip</title>
                                  <path d="M10 2a8 8 0 1 1-8 8 8 8 0 0 1 8-8m0-2a10 10 0 1 0 10 10A10 10 0 0 0 10 0z"/>
                                  <path d="M13.91 7.3a3 3 0 0 1-.13.93 2.75 2.75 0 0 1-.36.74 3.62 3.62 0 0 1-.56.63q-.33.3-.75.62l-.43.37a1.49 1.49 0 0 0-.27.33 1.27 1.27 0 0 0-.14.35 2.06 2.06 0 0 0 0 .44v.42H8.73v-.61a3.15 3.15 0 0 1 .08-.75 2.21 2.21 0 0 1 .24-.6 3.16 3.16 0 0 1 .39-.53 5.83 5.83 0 0 1 .56-.53l.53-.5a3.15 3.15 0 0 0 .47-.5 1.05 1.05 0 0 0 .19-.63 1.1 1.1 0 0 0-.31-.82 1.18 1.18 0 0 0-.86-.3 1.17 1.17 0 0 0-1 .46 1.88 1.88 0 0 0-.37 1l-2.56-.25A4.26 4.26 0 0 1 6.53 6a3.37 3.37 0 0 1 .89-1 3.79 3.79 0 0 1 1.24-.65 4.87 4.87 0 0 1 1.46-.22 5.39 5.39 0 0 1 1.41.18 3.58 3.58 0 0 1 1.21.58 2.92 2.92 0 0 1 .85 1 3.06 3.06 0 0 1 .32 1.41zm-2.36 7.09a1.46 1.46 0 0 1-.45 1.08 1.52 1.52 0 0 1-1.11.44 1.61 1.61 0 0 1-.6-.11 1.51 1.51 0 0 1-.5-.32 1.61 1.61 0 0 1-.33-.48 1.37 1.37 0 0 1-.13-.59 1.48 1.48 0 0 1 .12-.58 1.46 1.46 0 0 1 .34-.49 1.59 1.59 0 0 1 .5-.34 1.56 1.56 0 0 1 .61-.12 1.5 1.5 0 0 1 .6.12 1.7 1.7 0 0 1 .5.32 1.41 1.41 0 0 1 .34.48 1.49 1.49 0 0 1 .12.59z"/>
                                  <image class="icon--fallback" xlink:href="" src="/img/fallback/icon--tooltip.png">
                              </svg>
                            </button>
                            <div class="search__tooltip__text" aria-label="tooltip" role="alert">
                              <h3>What are Support Articles?</h3>
                              <p>Learn the basics of payments, how to best use Braintree features for your business, and what you can do to keep payments secure.</p>
                            </div>
                          </div>
                      </div>
                      <div class="hits--secondary">
                        <div class="hits__placeholder">Start typing to search</div>
                      </div>
                      <button class="button button--secondary button--small js-search-button-switch isHidden">More in Support Articles</button>
                    </div>
                  </div>
                  <div class="search__close">
                    <p class="search__close-message">Hit <span>ESC</span> to close</p>
                    <button class="search__button--close" aria-label="Press enter or hit escape to close">
                      <svg id="close" viewBox="0 0 24 24" class="icon--svg search__icon search__icon--close" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
                        <title>Close icon</title>
                        <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
                        <path d="M0 0h24v24H0z" fill="none"/>
                        <image class="icon--fallback" xlink:href="" src="/img/fallback/icon--close-x.png">
                      </svg>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          <div class="header__dropdown">
            <button class="dropdown__title button button--secondary button--small" aria-label="Access control panel" data-track-event-properties="project=journey,action=click,type=dropdown,container=header,descriptor=access control panel,intent=choose a control panel link">
              <span class="dropdown__title-text">Access Control Panel</span>
              <svg class="icon--svg dropdown__caret" viewBox="0 0 24 24" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
                  <title>Caret down</title>
                  <path d="M7.41 7.84L12 12.42l4.59-4.58L18 9.25l-6 6-6-6z"></path>
                  <path d="M0-.75h24v24H0z" fill="none"></path>
                  <image class="icon--fallback" xlink:href="" src="/img/fallback/icon--caret.png">
                </svg>
            </button>
            <div class="dropdown__content">
                <div class="dropdown__section">
                  <h3 class="dropdown__section-title">Sandbox</h3>
                  <ul class="dropdown__list">
                    <li class="dropdown__item">
                      <a class="link-list-link dropdown__link" href="https://sandbox.braintreegateway.com/login" target="_blank" data-track-event-properties="project=journey,action=click,type=link,descriptor=navbar sandbox login">Log in</a>
                    </li>
                    <li class="dropdown__item">
                      <a class="link-list-link dropdown__link" href="https://www.braintreepayments.com/sandbox" target="_blank" data-track-event-properties="project=journey,action=click,type=link,descriptor=navbar sandbox signup">Sign up</a>
                    </li>
                  </ul>
                </div>
                <div class="dropdown__section">
                  <h3 class="dropdown__section-title">Production</h3>
                  <ul class="dropdown__list">
                    <li class="dropdown__item">
                      <a class="link-list-link dropdown__link" href="https://www.braintreegateway.com/login" target="_blank" data-track-event-properties="project=journey,action=click,type=link,descriptor=navbar production login">Log in</a>
                    </li>
                    <li class="dropdown__item">
                      <a class="link-list-link dropdown__link" href="https://www.braintreepayments.com/" target="_blank" data-track-event-properties="project=journey,action=click,type=link,descriptor=navbar production signup">Sign up on <br />the website</a>
                    </li>
                  </ul>
                </div>
              </div>
          </div>
        </header>
<button class="button button--small menu__button js-off-canvas">
  <span class="menu__button-text">Menu</span>
</button>

<div class="flex-body">
  <div class="flex-sidebar documentation-sidebar">
    <div class="sidebar  ">
      <div class="sidebar__inner">
        <div class="sidebar__title">
          Developer Docs
        </div>
        <div class="menu-group">
          <span class="menu-group__title" data-title="">Client References</span>
          <ul class="menu">
                  <li class="menu__item">
                    <a target="_blank" href="http://www.javadoc.io/doc/com.braintreepayments.api/braintree" class="menu__link no-group icon is-external-link">Android<svg class="icon--svg icon--link--external" viewBox="0 0 15 15" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"><title>Link icon</title><g fill-rule="evenodd"><path d="M0 -0.0003L0 14.9997 15 14.9997 15 9.4757 13.235 9.4757 13.235 13.2347 1.765 13.2347 1.765 1.7647 5.524 1.7647 5.524 -0.0003z"/><path d="M8.685 -0.0003L8.685 1.7647 11.938 1.7647 4.579 9.1227 5.828 10.3717 13.235 2.9627 13.235 6.3137 15 6.3137 15 -0.0003z"/></g><image class="icon--fallback" xlink:href="" src="img/fallback/icon--link--external.png"></svg></a>
                  </li>
                  <li class="menu__item">
                    <a target="_blank" href="http://cocoadocs.org/docsets/Braintree" class="menu__link no-group icon is-external-link">iOS<svg class="icon--svg icon--link--external" viewBox="0 0 15 15" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"><title>Link icon</title><g fill-rule="evenodd"><path d="M0 -0.0003L0 14.9997 15 14.9997 15 9.4757 13.235 9.4757 13.235 13.2347 1.765 13.2347 1.765 1.7647 5.524 1.7647 5.524 -0.0003z"/><path d="M8.685 -0.0003L8.685 1.7647 11.938 1.7647 4.579 9.1227 5.828 10.3717 13.235 2.9627 13.235 6.3137 15 6.3137 15 -0.0003z"/></g><image class="icon--fallback" xlink:href="" src="img/fallback/icon--link--external.png"></svg></a>
                  </li>
                  <li class="menu__item">
                    <a target="_blank" href="https://braintree.github.io/braintree-web/current/" class="menu__link no-group icon is-external-link">JavaScript v3<svg class="icon--svg icon--link--external" viewBox="0 0 15 15" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"><title>Link icon</title><g fill-rule="evenodd"><path d="M0 -0.0003L0 14.9997 15 14.9997 15 9.4757 13.235 9.4757 13.235 13.2347 1.765 13.2347 1.765 1.7647 5.524 1.7647 5.524 -0.0003z"/><path d="M8.685 -0.0003L8.685 1.7647 11.938 1.7647 4.579 9.1227 5.828 10.3717 13.235 2.9627 13.235 6.3137 15 6.3137 15 -0.0003z"/></g><image class="icon--fallback" xlink:href="" src="img/fallback/icon--link--external.png"></svg></a>
                  </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    JavaScript v2
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/client-reference/javascript/v2/best-practices" class="menu-secondary__link ">Best Practices and Troubleshooting</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/client-reference/javascript/v2/browser-support" class="menu-secondary__link ">Browser Support</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/client-reference/javascript/v2/configuration" class="menu-secondary__link ">Configuration</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/client-reference/javascript/v2/credit-cards" class="menu-secondary__link ">Credit Cards</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/client-reference/javascript/v2/hosted-fields" class="menu-secondary__link ">Hosted Fields</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/client-reference/javascript/v2/paypal" class="menu-secondary__link ">PayPal</a>
                        </li>
                  </ul>
                </li>
          </ul>
        </div>
        <div class="menu-group">
          <span class="menu-group__title" data-title="">Server-Side API Requests</span>
          <ul class="menu">
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Add-On
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/add-on/all/java" class="menu-secondary__link ">All</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Address
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/address/create/java" class="menu-secondary__link ">Create</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/address/delete/java" class="menu-secondary__link ">Delete</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/address/find/java" class="menu-secondary__link ">Find</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/address/update/java" class="menu-secondary__link ">Update</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Apple Pay
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/apple-pay/register-domain/java" class="menu-secondary__link ">Register Domain</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/apple-pay/registered-domains/java" class="menu-secondary__link ">Registered Domains</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/apple-pay/unregister-domain/java" class="menu-secondary__link ">Unregister Domain</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Client Token
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/client-token/generate/java" class="menu-secondary__link ">Generate</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Credit Card
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/credit-card/create/java" class="menu-secondary__link ">Create</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/credit-card/delete/java" class="menu-secondary__link ">Delete</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/credit-card/expiring-between/java" class="menu-secondary__link ">Expiring Between</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/credit-card/find/java" class="menu-secondary__link ">Find</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/credit-card/update/java" class="menu-secondary__link ">Update</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Credit Card Verification
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/credit-card-verification/search/java" class="menu-secondary__link ">Search</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Customer
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/customer/create/java" class="menu-secondary__link ">Create</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/customer/delete/java" class="menu-secondary__link ">Delete</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/customer/find/java" class="menu-secondary__link ">Find</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/customer/search/java" class="menu-secondary__link ">Search</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/customer/update/java" class="menu-secondary__link ">Update</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Discount
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/discount/all/java" class="menu-secondary__link ">All</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Dispute
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/dispute/accept/java" class="menu-secondary__link ">Accept</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/dispute/add-file-evidence/java" class="menu-secondary__link ">Add File Evidence</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/dispute/add-text-evidence/java" class="menu-secondary__link ">Add Text Evidence</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/dispute/finalize/java" class="menu-secondary__link ">Finalize</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/dispute/find/java" class="menu-secondary__link ">Find</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/dispute/remove-evidence/java" class="menu-secondary__link ">Remove Evidence</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/dispute/search/java" class="menu-secondary__link ">Search</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Document Upload
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/document-upload/create/java" class="menu-secondary__link ">Create</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Merchant Account
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/merchant-account/all/java" class="menu-secondary__link ">All</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/merchant-account/create/java" class="menu-secondary__link ">Create</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/merchant-account/create-for-currency/java" class="menu-secondary__link ">Create For Currency</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/merchant-account/find/java" class="menu-secondary__link ">Find</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/merchant-account/update/java" class="menu-secondary__link ">Update</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Payment Method
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/payment-method/create/java" class="menu-secondary__link ">Create</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/payment-method/delete/java" class="menu-secondary__link ">Delete</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/payment-method/find/java" class="menu-secondary__link ">Find</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/payment-method/grant/java" class="menu-secondary__link ">Grant</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/payment-method/revoke/java" class="menu-secondary__link ">Revoke</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/payment-method/update/java" class="menu-secondary__link ">Update</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Payment Method Nonce
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/payment-method-nonce/create/java" class="menu-secondary__link ">Create</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/payment-method-nonce/find/java" class="menu-secondary__link ">Find</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Plan
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/plan/all/java" class="menu-secondary__link ">All</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Settlement Batch Summary
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/settlement-batch-summary/generate/java" class="menu-secondary__link ">Generate</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Subscription
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/subscription/cancel/java" class="menu-secondary__link ">Cancel</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/subscription/create/java" class="menu-secondary__link ">Create</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/subscription/find/java" class="menu-secondary__link ">Find</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/subscription/retry-charge/java" class="menu-secondary__link ">Retry Charge</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/subscription/search/java" class="menu-secondary__link ">Search</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/subscription/update/java" class="menu-secondary__link ">Update</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Transaction
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/transaction/cancel-release/java" class="menu-secondary__link ">Cancel Release</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/transaction/clone-transaction/java" class="menu-secondary__link ">Clone Transaction</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/transaction/find/java" class="menu-secondary__link ">Find</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/transaction/hold-in-escrow/java" class="menu-secondary__link ">Hold In Escrow</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/transaction/refund/java" class="menu-secondary__link ">Refund</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/transaction/release-from-escrow/java" class="menu-secondary__link ">Release From Escrow</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/transaction/sale/java" class="menu-secondary__link ">Sale</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/transaction/search/java" class="menu-secondary__link ">Search</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/transaction/submit-for-partial-settlement/java" class="menu-secondary__link ">Submit For Partial Settlement</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/transaction/submit-for-settlement/java" class="menu-secondary__link ">Submit For Settlement</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/request/transaction/void/java" class="menu-secondary__link ">Void</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Transaction Line Item
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/request/transaction-line-item/find-all/java" class="menu-secondary__link ">Find All</a>
                        </li>
                  </ul>
                </li>
          </ul>
        </div>
        <div class="menu-group">
          <span class="menu-group__title" data-title="">Server-Side Response Objects</span>
          <ul class="menu">
                  <li class="menu__item">
                    <a href="/reference/response/add-on/java" class="menu__link no-group">Add-On</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/address/java" class="menu__link no-group">Address</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/android-pay-card/java" class="menu__link no-group">Android Pay Card</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/apple-pay-card/java" class="menu__link no-group">Apple Pay Card</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/apple-pay-options/java" class="menu__link no-group">Apple Pay Options</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/credit-card/java" class="menu__link no-group">Credit Card</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/credit-card-verification/java" class="menu__link no-group">Credit Card Verification</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/customer/java" class="menu__link no-group">Customer</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/discount/java" class="menu__link no-group">Discount</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/dispute/java" class="menu__link no-group">Dispute</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/document-upload/java" class="menu__link no-group">Document Upload</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/masterpass-card/java" class="menu__link no-group">Masterpass Card</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/merchant-account/java" class="menu__link no-group">Merchant Account</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/paypal-account/java" class="menu__link no-group">PayPal Account</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/payment-method/java" class="menu__link no-group">Payment Method</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/payment-method-nonce/java" class="menu__link no-group">Payment Method Nonce</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/plan/java" class="menu__link no-group">Plan</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/settlement-batch-summary/java" class="menu__link no-group">Settlement Batch Summary</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/subscription/java" class="menu__link no-group">Subscription</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/transaction/java" class="menu__link no-group">Transaction</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/transaction-line-item/java" class="menu__link no-group">Transaction Line Item</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/venmo-account/java" class="menu__link no-group">Venmo Account</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/response/visa-checkout-card/java" class="menu__link no-group">Visa Checkout Card</a>
                  </li>
          </ul>
        </div>
        <div class="menu-group">
          <span class="menu-group__title" data-title="">General</span>
          <ul class="menu">
                  <li class="menu__item">
                    <a href="/reference/general/best-practices/java" class="menu__link no-group">Best Practices</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/general/class-level-vs-instance-methods/java" class="menu__link no-group">Class-Level vs Instance Methods</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/general/countries/java" class="menu__link no-group">Countries</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/general/currencies" class="menu__link no-group">Currencies</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/general/enterprise-third-party-plugins" class="menu__link no-group">Enterprise Third-Party Plugins</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/general/exceptions/java" class="menu__link no-group">Exceptions</a>
                  </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Processor Responses
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/general/processor-responses/authorization-responses" class="menu-secondary__link ">Authorization</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/general/processor-responses/settlement-responses" class="menu-secondary__link ">Settlement</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/general/processor-responses/avs-cvv-responses" class="menu-secondary__link ">AVS and CVV</a>
                        </li>
                  </ul>
                </li>
                  <li class="menu__item">
                    <a href="/reference/general/proxy-servers/java" class="menu__link no-group">Proxy Servers</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/general/result-objects/java" class="menu__link no-group">Result Objects</a>
                  </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Searching
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/general/searching/search-fields/java" class="menu-secondary__link ">Search Fields</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/general/searching/search-results/java" class="menu-secondary__link ">Search Results</a>
                        </li>
                  </ul>
                </li>
                  <li class="menu__item">
                    <a href="/reference/general/statuses" class="menu__link no-group">Statuses</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/general/testing/java" class="menu__link no-group">Testing</a>
                  </li>
                  <li class="menu__item">
                    <a href="/reference/general/upgrade" class="menu__link no-group">Upgrade to Braintree SDKs</a>
                  </li>
                <li class="menu__item js-menu-item is-open auto-open">
                  <span class="menu__link has-menu" tabindex="0">
                    Validation Errors
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/general/validation-errors/overview/java" class="menu-secondary__link ">Overview</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/general/validation-errors/all/java" class="menu-secondary__link  is-active">Validation Errors</a>
                        </li>
                  </ul>
                </li>
                <li class="menu__item js-menu-item ">
                  <span class="menu__link has-menu" tabindex="0">
                    Webhooks
                  </span>
                  <ul class="menu-secondary">
                        <li class="menu-secondary__item">
                          <a href="/reference/general/webhooks/overview" class="menu-secondary__link ">Overview</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/general/webhooks/braintree-auth/java" class="menu-secondary__link ">Braintree Auth</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/general/webhooks/disbursement/java" class="menu-secondary__link ">Disbursement</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/general/webhooks/dispute/java" class="menu-secondary__link ">Dispute</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/general/webhooks/grant-api/java" class="menu-secondary__link ">Grant API</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/general/webhooks/sub-merchant-account/java" class="menu-secondary__link ">Sub-merchant Account</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/general/webhooks/subscription/java" class="menu-secondary__link ">Subscription</a>
                        </li>
                        <li class="menu-secondary__item">
                          <a href="/reference/general/webhooks/test/java" class="menu-secondary__link ">Test</a>
                        </li>
                  </ul>
                </li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="flex-content documentation-content__wrapper">
    <div class="page-header page-header--guides">
      <div class="page-header__inner">
        <h1 class="page-header__title-group">
          <span class="page-header__section">Validation Errors<span class="page-header--title-divider">/</span></span><span class="page-header__title">All</span>
        </h1>
        <div class="page-header__picker sdk-picker cf">
          <div class="sdk-picker__wrapper">
            <div class="js-sdk-picker__trigger sdk-picker__button button button--small">
              <span class="sdk-picker__title"></span>
              <span class="sdk-picker__description">SDK</span>
              <svg class="icon--svg icon--caret sdk-picker__caret" viewBox="0 0 24 24" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
                <title>Caret down</title>
                <path d="M7.41 7.84L12 12.42l4.59-4.58L18 9.25l-6 6-6-6z"></path>
                <path d="M0-.75h24v24H0z" fill="none"></path>
                <image class="icon--fallback" xlink:href="" src="img/fallback/icon--caret.png">
              </svg>
            </div>
            <ul class="sdk-picker__list"><li class="sdk-picker__menu-title">CURRENT BRAINTREE SDKS</li><li class="sdk-picker__item"><a href="/reference/general/validation-errors/all/java" data-title="Java" data-value="/java" class="sdk-picker__link is-active">Java</a></li><li class="sdk-picker__item"><a href="/reference/general/validation-errors/all/dotnet" data-title=".Net" data-value="/dotnet" class="sdk-picker__link">.Net</a></li><li class="sdk-picker__item"><a href="/reference/general/validation-errors/all/node" data-title="Node.js" data-value="/node" class="sdk-picker__link">Node.js</a></li><li class="sdk-picker__item"><a href="/reference/general/validation-errors/all/php" data-title="PHP" data-value="/php" class="sdk-picker__link">PHP</a></li><li class="sdk-picker__item"><a href="/reference/general/validation-errors/all/python" data-title="Python" data-value="/python" class="sdk-picker__link">Python</a></li><li class="sdk-picker__item"><a href="/reference/general/validation-errors/all/ruby" data-title="Ruby" data-value="/ruby" class="sdk-picker__link">Ruby</a></li></ul>
          </div>
        </div>
        
      </div>
    </div>
    <hr class="page-rule" />

    <article class="flex--constrained main-content js-outlet js-reference-view">
      <h1 class="markdown-h1">
  All Validation Errors
  <a class="icon icon--link hash-link" href="#all-validation-errors">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="all-validation-errors"></a>
</h1>
<ul class="list list--disc"><li><a href="#address">Address</a></li>
<li><a href="#braintree-auth">Braintree Auth</a><ul class="list list--disc"><li><a href="#auth-merchants">Auth Merchants</a></li>
</ul>
</li>
<li><a href="#braintree-marketplace">Braintree Marketplace</a><ul class="list list--disc"><li><a href="#merchant-account">Merchant Account</a></li>
</ul>
</li>
<li><a href="#client-token">Client Token</a></li>
<li><a href="#customer">Customer</a></li>
<li><a href="#payment-method">Payment Method</a><ul class="list list--disc"><li><a href="#apple-pay">Apple Pay</a></li>
<li><a href="#credit-card">Credit Card</a><ul class="list list--disc"><li><a href="#american-express-industry-data">American Express Industry Data</a></li>
</ul>
</li>
<li><a href="#paypal">PayPal</a></li>
<li><a href="#venmo">Venmo</a></li>
</ul>
</li>
<li><a href="#recurring-billing">Recurring Billing</a><ul class="list list--disc"><li><a href="#add-ons/discounts">Add-ons/Discounts</a></li>
<li><a href="#subscription">Subscription</a></li>
</ul>
</li>
<li><a href="#search">Search</a></li>
<li><a href="#transaction">Transaction</a><ul class="list list--disc"><li><a href="#authorization-adjustment">Authorization Adjustment</a></li>
<li><a href="#descriptor">Descriptor</a></li>
<li><a href="#transaction-line-items">Transaction Line Items</a></li>
</ul>
</li>
<li><a href="#verification">Verification</a></li>
</ul>
<h2 class="markdown-h2">
  Address
  <a class="icon icon--link hash-link" href="#address">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="address"></a>
</h2>
<p class="markdown-p">These validations apply when creating or updating addresses in the Vault directly, and also when providing billing and shipping details in requests like <a href="/reference/request/transaction/sale/java"><code class="syntax-inline syntax-inline--theme">Transaction.sale()</code></a> or <a href="/reference/request/payment-method/create/java"><code class="syntax-inline syntax-inline--theme">PaymentMethod.create()</code></a>.</p>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-81801" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81801</code></td><td>Addresses must have at least one field filled in.</td><td><p class="markdown-p">At least one of the address attributes must be present, but it doesn&#39;t matter which one. This doesn&#39;t apply when creating transactions&mdash;billing and shipping address can be blank unless <a href="https://articles.braintreepayments.com/guides/fraud-tools/basic/avs-cvv-rules">AVS processing rules</a> are configured to require billing street and postal.</p></td></tr>
    <tr id="code-81802" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81802</code></td><td>Company is too long.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-81804" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81804</code></td><td>Extended address is too long.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-81805" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81805</code></td><td>First name is too long.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-81806" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81806</code></td><td>Last name is too long.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-81807" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81807</code></td><td>Locality is too long.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-81813" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81813</code></td><td>Postal code can only contain letters, numbers, spaces, and hyphens.</td><td><p class="markdown-p">There are also length limitations, but that&#39;s a different validation error.</p></td></tr>
    <tr id="code-81808" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81808</code></td><td>Postal code is required.</td><td><p class="markdown-p">Applies when AVS rules are configured to require postal code.</p></td></tr>
    <tr id="code-81809" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81809</code></td><td>Postal code may contain no more than 9 letter or number characters.</td><td><p class="markdown-p">The length only applies to letters or numbers; it ignores spaces, hyphens, and all other special characters.</p></td></tr>
    <tr id="code-81810" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81810</code></td><td>Region is too long.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-81811" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81811</code></td><td>Street address is required.</td><td><p class="markdown-p">Applies when creating a transaction or performing card verification when AVS rules are configured to require street address.</p></td></tr>
    <tr id="code-81812" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81812</code></td><td>Street address is too long.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-81827" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81827</code></td><td>US state codes must be two characters to meet PayPal Seller Protection requirements.</td><td><p class="markdown-p">US state codes must be two characters to meet PayPal Seller Protection requirements.</p></td></tr>
    <tr id="code-91803" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91803</code></td><td>Country name is not an accepted country.</td><td><p class="markdown-p">We only accept <a href="/reference/general/countries">specific country names</a>.</p></td></tr>
    <tr id="code-91815" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91815</code></td><td>Provided country information is inconsistent.</td><td><p class="markdown-p">You can only specify one of country name, country code alpha2, country code alpha3 and country code numeric.</p></td></tr>
    <tr id="code-91816" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91816</code></td><td>Country code (alpha3) is not an accepted country.</td><td><p class="markdown-p">We only accept <a href="/reference/general/countries#list-of-countries">specific alpha-3 values</a>.</p></td></tr>
    <tr id="code-91817" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91817</code></td><td>Country code (numeric) is not an accepted country.</td><td><p class="markdown-p">We only accept <a href="/reference/general/countries#list-of-countries">specific numeric values</a>.</p></td></tr>
    <tr id="code-91814" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91814</code></td><td>Country code (alpha2) is not an accepted country.</td><td><p class="markdown-p">We only accept <a href="/reference/general/countries#list-of-countries">specific alpha-2 values</a>.</p></td></tr>
    <tr id="code-91818" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91818</code></td><td>Customer has already reached the maximum of 50 addresses.</td><td><p class="markdown-p">You will get this validation error when trying to add an address to a customer which has already reached the maximum of 50 addresses.</p></td></tr>
    <tr id="code-91819" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91819</code></td><td>First name must be a string.</td><td><p class="markdown-p">First name must be a string.</p></td></tr>
    <tr id="code-91820" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91820</code></td><td>Last name must be a string.</td><td><p class="markdown-p">Last name must be a string.</p></td></tr>
    <tr id="code-91821" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91821</code></td><td>Company must be a string.</td><td><p class="markdown-p">Company must be a string.</p></td></tr>
    <tr id="code-91822" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91822</code></td><td>Street address must be a string.</td><td><p class="markdown-p">Street address must be a string.</p></td></tr>
    <tr id="code-91823" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91823</code></td><td>Extended address must be a string.</td><td><p class="markdown-p">Extended address must be a string.</p></td></tr>
    <tr id="code-91824" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91824</code></td><td>Locality must be a string.</td><td><p class="markdown-p">Locality must be a string.</p></td></tr>
    <tr id="code-91825" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91825</code></td><td>Region must be a string.</td><td><p class="markdown-p">Region must be a string.</p></td></tr>
    <tr id="code-91826" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91826</code></td><td>Postal code must be a string.</td><td><p class="markdown-p">Postal code must be a string.</p></td></tr>
    <tr id="code-91828" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91828</code></td><td>Address is invalid.</td><td><p class="markdown-p">Address must provided in a <a href="/reference/request/address/create">valid format</a>.</p></td></tr>
  </tbody>
</table>

<h2 class="markdown-h2">
  Braintree Auth
  <a class="icon icon--link hash-link" href="#braintree-auth">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="braintree-auth"></a>
</h2>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-93801" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93801</code></td><td>Invalid grant: </td><td><p class="markdown-p">The provided authorization grant (e.g. authorization code, resource owner credentials) or refresh token is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client.</p></td></tr>
    <tr id="code-93802" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93802</code></td><td>Invalid credentials: </td><td><p class="markdown-p">Client authentication failed (e.g. unknown client, no client authentication included, or unsupported authentication method).</p></td></tr>
    <tr id="code-93803" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93803</code></td><td>Invalid scope: </td><td><p class="markdown-p">The requested scope is invalid, unknown, malformed, or exceeds the scope granted by the resource owner.</p></td></tr>
    <tr id="code-93804" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93804</code></td><td>Invalid request: </td><td><p class="markdown-p">The request is missing a required parameter, includes an unsupported parameter value (other than grant type), repeats a parameter, includes multiple credentials, utilizes more than one mechanism for authenticating the client, or is otherwise malformed.</p></td></tr>
    <tr id="code-93805" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93805</code></td><td>Unsupported grant type: </td><td><p class="markdown-p">The authorization grant type is not supported by the authorization server.</p></td></tr>
  </tbody>
</table>

<h3 class="markdown-h3">
  Auth merchants
  <a class="icon icon--link hash-link" href="#auth-merchants">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="auth-merchants"></a>
</h3>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-93618" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93618</code></td><td>Currency passed is not accepted.</td><td><p class="markdown-p">The currency passed is not one of the <a href="/guides/braintree-auth/multi-currency#currency-support">supported currencies</a>.</p></td></tr>
    <tr id="code-93621" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93621</code></td><td>Merchant account was not OAuth onboarded.</td><td><p class="markdown-p">Merchant was not onboarded through <a href="/guides/braintree-auth/overview">Braintree Auth</a>.</p></td></tr>
    <tr id="code-93622" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93622</code></td><td>Company name is not valid</td><td><p class="markdown-p">The applicant&#39;s company name must contain only letters, numbers, and these characters: <code class="syntax-inline syntax-inline--theme">&amp;-!@#$()&#39;./+,&quot;</code>. The maximum length is 40 characters.</p></td></tr>



















  </tbody>
</table>

<h2 class="markdown-h2">
  Braintree Marketplace
  <a class="icon icon--link hash-link" href="#braintree-marketplace">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="braintree-marketplace"></a>
</h2>
<h3 class="markdown-h3">
  Merchant Account
  <a class="icon icon--link hash-link" href="#merchant-account">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="merchant-account"></a>
</h3>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-82602" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82602</code></td><td>Applicant merchant id is too long.</td><td><p class="markdown-p">The merchant account id cannot be longer than 32 characters.</p></td></tr>
    <tr id="code-82603" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82603</code></td><td>Applicant merchant id format is invalid.</td><td><p class="markdown-p">You can only use letters, numbers, _ and - for the merchant account id.</p></td></tr>
    <tr id="code-82604" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82604</code></td><td>Applicant merchant id is in use.</td><td><p class="markdown-p">Merchant account ids need to be unique.</p></td></tr>
    <tr id="code-82605" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82605</code></td><td>Applicant merchant id is not allowed.</td><td><p class="markdown-p">Merchant account ids may not be named &#39;all&#39; or &#39;new.&#39;</p></td></tr>
    <tr id="code-82606" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82606</code></td><td>Master merchant account ID is required.</td><td><p class="markdown-p">You must provide a master merchant account id when creating a merchant account.</p></td></tr>
    <tr id="code-82607" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82607</code></td><td>Master merchant account ID is invalid.</td><td><p class="markdown-p">You&#39;ll get this error if we cannot find a master merchant account with the id specified.</p></td></tr>
    <tr id="code-82608" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82608</code></td><td>Master merchant account must be active.</td><td><p class="markdown-p">You&#39;ll get this error if the supplied master merchant account id is not active.</p></td></tr>
    <tr id="code-82610" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82610</code></td><td>Terms Of Service needs to be accepted. Applicant tos_accepted required.</td><td><p class="markdown-p">You must indicate that the terms of service are accepted.</p></td></tr>
    <tr id="code-82675" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82675</code></td><td>Merchant account id can not be updated.</td><td><p class="markdown-p">You&#39;ll get this error if the ID cannot be updated.</p></td></tr>
    <tr id="code-82676" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82676</code></td><td>Master merchant account id can not be updated.</td><td><p class="markdown-p">You&#39;ll get this error if the merchant account ID cannot be updated.</p></td></tr>
    <tr id="code-82674" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82674</code></td><td>Merchant accounts with a status of pending or suspended cannot be updated.</td><td><p class="markdown-p">The merchant account cannot be updated.</p></td></tr>
    <tr id="code-82609" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82609</code></td><td>Applicant first name is required.</td><td><p class="markdown-p">You must provide the first name of the applicant.</p></td></tr>
    <tr id="code-82637" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82637</code></td><td>Individual first name is required.</td><td><p class="markdown-p">Applicant first name is required.</p></td></tr>
    <tr id="code-82611" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82611</code></td><td>Applicant last name is required.</td><td><p class="markdown-p">You must provide the last name of the applicant.</p></td></tr>
    <tr id="code-82638" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82638</code></td><td>Individual last name is required.</td><td><p class="markdown-p">Applicant last name is required.</p></td></tr>
    <tr id="code-82612" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82612</code></td><td>Applicant date of birth is required.</td><td><p class="markdown-p">You must provide the applicant&#39;s date of birth.</p></td></tr>
    <tr id="code-82639" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82639</code></td><td>Individual date of birth is required.</td><td><p class="markdown-p">Individual date of birth is required.</p></td></tr>
    <tr id="code-82613" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82613</code></td><td>Applicant routing number is required.</td><td><p class="markdown-p">You must provide the applicant&#39;s bank routing number.</p></td></tr>
    <tr id="code-82640" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82640</code></td><td>Funding routing number is required.</td><td><p class="markdown-p">Funding routing number is required.</p></td></tr>
    <tr id="code-82614" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82614</code></td><td>Applicant account number is required.</td><td><p class="markdown-p">You must provide the applicant&#39;s bank account number.</p></td></tr>
    <tr id="code-82641" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82641</code></td><td>Funding account number is required.</td><td><p class="markdown-p">Funding account number is required.</p></td></tr>
    <tr id="code-82615" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82615</code></td><td>Applicant SSN must be blank, last 4 digits, or full 9 digits.</td><td><p class="markdown-p">The applicant&#39;s social security number must be valid (full 9 digits, with or without dashes, or last 4 digits).</p></td></tr>
    <tr id="code-82642" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82642</code></td><td>Individual SSN must be blank, last 4 digits, or full 9 digits.</td><td><p class="markdown-p">Individual SSN must be blank, last 4 digits, or full 9 digits.</p></td></tr>
    <tr id="code-82616" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82616</code></td><td>Applicant email is invalid.</td><td><p class="markdown-p">The applicant&#39;s email must be valid.</p></td></tr>
    <tr id="code-82643" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82643</code></td><td>Individual email is invalid.</td><td><p class="markdown-p">Individual email is invalid.</p></td></tr>
    <tr id="code-82627" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82627</code></td><td>Applicant first name is invalid.</td><td><p class="markdown-p">The applicant&#39;s first name must not contain &#39;/&#39;, &#39;\&#39;, &#39;&amp;&#39;, &#39;&lt;&#39;, &#39;&gt;&#39; or any control characters.</p></td></tr>
    <tr id="code-82644" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82644</code></td><td>Individual first name is invalid.</td><td><p class="markdown-p">Individual first name is invalid.</p></td></tr>
    <tr id="code-82628" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82628</code></td><td>Applicant last name is invalid.</td><td><p class="markdown-p">The applicant&#39;s last name must not contain &#39;/&#39;, &#39;\&#39;, &#39;&amp;&#39;, &#39;&lt;&#39;, &#39;&gt;&#39; or any control characters.</p></td></tr>
    <tr id="code-82645" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82645</code></td><td>Individual last name is invalid.</td><td><p class="markdown-p">Applicant last name is invalid.</p></td></tr>
    <tr id="code-82631" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82631</code></td><td>Applicant company name is invalid.</td><td><p class="markdown-p">The applicant&#39;s company name must contain only letters, numbers, and these characters: <code class="syntax-inline syntax-inline--theme">&amp;-!@#$()&#39;./+,&quot;</code>. The maximum length is 40 characters.</p></td></tr>
    <tr id="code-82632" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82632</code></td><td>Applicant tax ID is invalid.</td><td><p class="markdown-p">The applicant&#39;s tax id must be 9 digits long.</p></td></tr>
    <tr id="code-82688" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82688</code></td><td>Business params provided in an invalid format.</td><td><p class="markdown-p">You must provide the attributes for Business in the correct format.</p></td></tr>
    <tr id="code-82647" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82647</code></td><td>Business tax ID is invalid.</td><td><p class="markdown-p">Business tax ID is invalid.</p></td></tr>
    <tr id="code-82633" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82633</code></td><td>Applicant company name is required with tax ID.</td><td><p class="markdown-p">If the applicant&#39;s tax id is provided then the company name must be provided as well.</p></td></tr>
    <tr id="code-82634" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82634</code></td><td>Applicant tax ID is required with company name.</td><td><p class="markdown-p">If the applicant&#39;s company name is provided then the tax id must be provided as well.</p></td></tr>
    <tr id="code-82635" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82635</code></td><td>Applicant routing number is invalid.</td><td><p class="markdown-p">The applicant&#39;s bank routing number must be valid.</p></td></tr>
    <tr id="code-82649" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82649</code></td><td>Funding routing number is invalid.</td><td><p class="markdown-p">Funding routing number is invalid.</p></td></tr>
    <tr id="code-82650" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82650</code></td><td>An unexpected error occurred trying to save the merchant account; support has been notified and is looking into the issue.  You may safely retry this request</td><td><p class="markdown-p">An unexpected error occurred trying to save the merchant account; Support has been notified and is looking into the issue. You may safely retry this request.</p></td></tr>
    <tr id="code-82621" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82621</code></td><td>Applicant declined due to OFAC.</td><td><p class="markdown-p">The applicant has failed an OFAC check. The OFAC search confirms whether a sub-merchant is on the criminal and terrorists watch lists collected from databases around the world.</p></td></tr>
    <tr id="code-82622" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82622</code></td><td>Applicant declined due to MasterCard MATCH.</td><td><p class="markdown-p">The applicant has failed a Mastercard MATCH check. The Mastercard MATCH File is a database file used by payment processing banks to identify specific merchants and principals who may been terminated for reasons like fraud or violation(s) of Visa and/or Mastercard rules.</p></td></tr>
    <tr id="code-82623" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82623</code></td><td>Applicant declined due to failed KYC.</td><td><p class="markdown-p">The applicant has failed a Know Your Customer check.</p></td></tr>
    <tr id="code-82624" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82624</code></td><td>Applicant declined due to invalid SSN.</td><td><p class="markdown-p">The applicant&#39;s social security number is invalid. If you provide a social security number, you must provide either the entire number or the last four digits.</p></td></tr>
    <tr id="code-82625" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82625</code></td><td>Applicant declined due to SSN matching that of a deceased person.</td><td><p class="markdown-p">The applicant has been declined because the social security number provided appears in a database of social security numbers belonging to deceased persons.</p></td></tr>
    <tr id="code-82626" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82626</code></td><td>Applicant declined after review.</td><td><p class="markdown-p">After review, the applicant has been declined.</p></td></tr>
    <tr id="code-82617" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82617</code></td><td>Applicant street address is required.</td><td><p class="markdown-p">You must provide the applicant&#39;s street address.</p></td></tr>
    <tr id="code-82657" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82657</code></td><td>Individual street address is required.</td><td><p class="markdown-p">Individual street address is required.</p></td></tr>
    <tr id="code-82618" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82618</code></td><td>Applicant locality is required.</td><td><p class="markdown-p">You must provide the applicant&#39;s city, town, or municipality.</p></td></tr>
    <tr id="code-82658" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82658</code></td><td>Individual locality is required.</td><td><p class="markdown-p">Individual locality is required.</p></td></tr>
    <tr id="code-82619" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82619</code></td><td>Applicant postal code is required.</td><td><p class="markdown-p">You must provide the applicant&#39;s postal code.</p></td></tr>
    <tr id="code-82659" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82659</code></td><td>Individual postal code is required.</td><td><p class="markdown-p">Individual postal code is required.</p></td></tr>
    <tr id="code-82620" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82620</code></td><td>Applicant region is required.</td><td><p class="markdown-p">You must provide the applicant&#39;s region.</p></td></tr>
    <tr id="code-82660" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82660</code></td><td>Individual region is required.</td><td><p class="markdown-p">Individual region is required.</p></td></tr>
    <tr id="code-82629" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82629</code></td><td>Applicant street address is invalid.</td><td><p class="markdown-p">You must provide a valid street address for the applicant that includes at least one digit.</p></td></tr>
    <tr id="code-82661" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82661</code></td><td>Individual street address is invalid.</td><td><p class="markdown-p">Individual street address is invalid.</p></td></tr>
    <tr id="code-82664" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82664</code></td><td>Applicant region is invalid.</td><td><p class="markdown-p">You must provide a valid region for the applicant. Only two-letter abbreviations are accepted, e.g. &#39;CA&#39; but not &#39;California.&#39;</p></td></tr>
    <tr id="code-82668" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82668</code></td><td>Individual region is invalid.</td><td><p class="markdown-p">Individual region is invalid.</p></td></tr>
    <tr id="code-82630" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82630</code></td><td>Applicant postal code is invalid.</td><td><p class="markdown-p">You must provide a valid postal code for the applicant.</p></td></tr>
    <tr id="code-82662" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82662</code></td><td>Individual postal code is invalid.</td><td><p class="markdown-p">Individual postal code is invalid.</p></td></tr>
    <tr id="code-82636" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82636</code></td><td>Applicant phone is invalid.</td><td><p class="markdown-p">The provided phone is not valid.</p></td></tr>
    <tr id="code-82656" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82656</code></td><td>Individual phone is invalid.</td><td><p class="markdown-p">Individual phone is invalid.</p></td></tr>
    <tr id="code-82663" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82663</code></td><td>Applicant date of birth is invalid</td><td><p class="markdown-p">You must provide a valid date of birth.</p></td></tr>
    <tr id="code-82666" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82666</code></td><td>Individual date of birth is invalid.</td><td><p class="markdown-p">Individual date of birth is invalid.</p></td></tr>
    <tr id="code-82670" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82670</code></td><td>Applicant account number is invalid.</td><td><p class="markdown-p">The provided bank account number is not valid.</p></td></tr>
    <tr id="code-82671" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82671</code></td><td>Funding account number is invalid.</td><td><p class="markdown-p">Funding account number is invalid.</p></td></tr>
    <tr id="code-82665" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82665</code></td><td>Applicant email is required.</td><td><p class="markdown-p">You must provide an email address.</p></td></tr>
    <tr id="code-82667" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82667</code></td><td>Individual email is required.</td><td><p class="markdown-p">Individual email is required.</p></td></tr>
    <tr id="code-82672" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82672</code></td><td>Business tax ID must be blank unless business legal name is present.</td><td><p class="markdown-p">The tax id must be blank if no company name/legal name is provided.</p></td></tr>
    <tr id="code-82673" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82673</code></td><td>Applicant tax ID must be blank unless company name present.</td><td><p class="markdown-p">Applicant tax ID must be blank unless company name present.</p></td></tr>
    <tr id="code-82646" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82646</code></td><td>Business DBA name is invalid.</td><td><p class="markdown-p">The provided DBA name is not valid. The applicant&#39;s company name must contain only letters, numbers, and these characters: <code class="syntax-inline syntax-inline--theme">&amp;-!@#$()&#39;./+,&quot;</code>. The maximum length is 40 characters.</p></td></tr>
    <tr id="code-82677" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82677</code></td><td>Business legal name is invalid.</td><td><p class="markdown-p">The provided legal name is not valid. The applicant&#39;s company name must contain only letters, numbers, and these characters: <code class="syntax-inline syntax-inline--theme">&amp;-!@#$()&#39;./+,&quot;</code>. The maximum length is 40 characters.</p></td></tr>
    <tr id="code-82669" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82669</code></td><td>Business legal name is required with tax ID.</td><td><p class="markdown-p">You must provide a legal name if a tax id has been provided.</p></td></tr>
    <tr id="code-82648" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82648</code></td><td>Business tax ID is required with business legal name.</td><td><p class="markdown-p">You must provide a tax id if a legal name has been provided.</p></td></tr>
    <tr id="code-82685" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82685</code></td><td>Business street address is invalid.</td><td><p class="markdown-p">The provided business street address is not valid. It must contain at least one digit.</p></td></tr>
    <tr id="code-82686" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82686</code></td><td>Business postal code is invalid.</td><td><p class="markdown-p">The provided business zip code is not valid. It must be 5 digits followed by an optional hyphen, space, and an additional 4 digits.</p></td></tr>
    <tr id="code-82684" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82684</code></td><td>Business region is invalid.</td><td><p class="markdown-p">The provided business region is not valid. Only two-letter abbreviations are accepted, e.g. &#39;CA&#39; but not &#39;California.&#39;</p></td></tr>
    <tr id="code-82679" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82679</code></td><td>Funding destination is invalid.</td><td><p class="markdown-p">You must provide a valid funding destination.</p></td></tr>
    <tr id="code-82678" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82678</code></td><td>Funding destination is required.</td><td><p class="markdown-p">You must provide a funding destination.</p></td></tr>
    <tr id="code-82681" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82681</code></td><td>Funding email is invalid.</td><td><p class="markdown-p">The provided funding email address is not valid.</p></td></tr>
    <tr id="code-82680" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82680</code></td><td>Funding email is required when destination is email.</td><td><p class="markdown-p">You must provide a funding email address when your funding destination is email.</p></td></tr>
    <tr id="code-82683" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82683</code></td><td>Funding mobile phone is invalid.</td><td><p class="markdown-p">The provided funding mobile phone is not valid. Phone must be 10 - 14 characters and can only contain numbers, parentheses, and periods.</p></td></tr>
    <tr id="code-82682" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82682</code></td><td>Funding mobile phone is required when destination is mobile phone.</td><td><p class="markdown-p">You must provide a funding mobile phone when your funding destination is mobile phone.</p></td></tr>
    <tr id="code-82687" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82687</code></td><td>Individual params provided in an invalid format.</td><td><p class="markdown-p">You must provide the attributes for Individual in the correct format.</p></td></tr>
    <tr id="code-82689" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82689</code></td><td>Business locality is invalid.</td><td><p class="markdown-p">The provided business address is not valid.</p></td></tr>
    <tr id="code-82690" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82690</code></td><td>Individual locality is invalid.</td><td><p class="markdown-p">The provided individual address is not valid.</p></td></tr>
    <tr id="code-82691" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82691</code></td><td>Applicant locality is invalid.</td><td><p class="markdown-p">The provided applicant address is not valid.</p></td></tr>
  </tbody>
</table>

<h2 class="markdown-h2">
  Client Token
  <a class="icon icon--link hash-link" href="#client-token">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="client-token"></a>
</h2>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-92801" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92801</code></td><td>Cannot specify make_default without a customer_id</td><td><p class="markdown-p">Cannot specify make_default without a customer_id</p></td></tr>
    <tr id="code-92802" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92802</code></td><td>Cannot specify verify_card without a customer_id</td><td><p class="markdown-p">Cannot specify verify_card without a customer_id</p></td></tr>
    <tr id="code-92803" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92803</code></td><td>Cannot specify fail_on_duplicate_payment_method without a customer_id</td><td><p class="markdown-p">Cannot specify fail_on_duplicate_payment_method without a customer_id</p></td></tr>
    <tr id="code-92804" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92804</code></td><td>Customer specified by customer_id does not exist</td><td><p class="markdown-p">Customer specified by customer_id does not exist</p></td></tr>
    <tr id="code-92806" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92806</code></td><td>Unsupported client token version</td><td><p class="markdown-p">Unsupported client token version</p></td></tr>
    <tr id="code-92807" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92807</code></td><td>Merchant Account specified by merchant_account_id does not exist</td><td><p class="markdown-p">Merchant Account specified by merchant_account_id does not exist</p></td></tr>
  </tbody>
</table>

<h2 class="markdown-h2">
  Customer
  <a class="icon icon--link hash-link" href="#customer">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="customer"></a>
</h2>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-91602" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91602</code></td><td>Custom field is invalid: </td><td><p class="markdown-p">Custom field keys must match the API name of a <a href="https://articles.braintreepayments.com/control-panel/custom-fields">custom field configured in the Control Panel</a>. The error message for this validation error will contain a list of the invalid keys.</p></td></tr>
    <tr id="code-91609" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91609</code></td><td>Customer ID has already been taken.</td><td><p class="markdown-p">Customer IDs have to be unique.</p></td></tr>
    <tr id="code-91610" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91610</code></td><td>Customer ID is invalid (use only letters, numbers, &#39;-&#39;, and &#39;_&#39;).</td><td><p class="markdown-p">Valid characters are letters, numbers, dashes, and underscores.</p></td></tr>
    <tr id="code-91611" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91611</code></td><td>Customer ID is not an allowed ID.</td><td><p class="markdown-p">We reserve a few words that can&#39;t be used as IDs. &#39;all&#39; and &#39;new&#39; currently cannot be used.</p></td></tr>
    <tr id="code-91612" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91612</code></td><td>Customer ID is too long.</td><td><p class="markdown-p">Maximum 36 characters.</p></td></tr>
    <tr id="code-91613" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91613</code></td><td>Customer ID is required.</td><td><p class="markdown-p">Customer ID is required when performing updates.</p></td></tr>
    <tr id="code-91617" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91617</code></td><td>Nonce references a vaulted payment instrument - cannot be transferred between customers</td><td><p class="markdown-p">Nonce references a vaulted payment instrument - cannot be transferred between customers.</p></td></tr>
    <tr id="code-91618" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91618</code></td><td>Customer attribute must be a map of keys and values representing a customer.</td><td><p class="markdown-p">Customer must be a well-formed object, not a string or integer.</p></td></tr>
    <tr id="code-91619" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91619</code></td><td>Ambiguous usage of default payment method token.</td><td><p class="markdown-p">Cannot set <a href="/reference/request/customer/update/java#default_payment_method_token"><code class="syntax-inline syntax-inline--theme">defaultPaymentMethodToken()</code></a> and <a href="/reference/request/customer/update/java#credit_card.options.make_default"><code class="syntax-inline syntax-inline--theme">creditCard().options().makeDefault()</code></a> in the same customer update request.</p></td></tr>
    <tr id="code-91620" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91620</code></td><td>PayPal custom field must be less than 256 characters in length.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-91621" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91621</code></td><td>PayPal description must be less than 256 characters in length.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-91622" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91622</code></td><td>Order ID must be less than 256 characters in length.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-91623" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91623</code></td><td>Amount format is invalid.</td><td><p class="markdown-p">Amount must be formatted like &#39;10&#39; or &#39;10.00&#39;.</p></td></tr>
    <tr id="code-81601" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81601</code></td><td>Company is too long.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-81603" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81603</code></td><td>Custom field is too long: </td><td><p class="markdown-p">Custom field values must be less than or equal to 255 characters. The error message for this validation error will contain a list of the custom fields that were too long.</p></td></tr>
    <tr id="code-81604" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81604</code></td><td>Email is an invalid format.</td><td><p class="markdown-p">Email must be a well-formed email address. If you are migrating from a system that does not have this constraint and want to record the email address in the Vault, you can use <a href="/reference/request/customer/create/java#custom_fields"><code class="syntax-inline syntax-inline--theme">customFields()</code></a></p></td></tr>
    <tr id="code-81605" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81605</code></td><td>Email is too long.</td><td><p class="markdown-p">Maximum 254 characters.</p></td></tr>
    <tr id="code-81606" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81606</code></td><td>Email is required if sending a receipt.</td><td><p class="markdown-p">This only applies when creating a transaction. If you specify that you want to send a receipt then the customer email will be required.</p></td></tr>
    <tr id="code-81607" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81607</code></td><td>Fax is too long.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-81608" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81608</code></td><td>First name is too long.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-81613" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81613</code></td><td>Last name is too long.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-81614" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81614</code></td><td>Phone is too long.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-81615" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81615</code></td><td>Website is too long.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-81616" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81616</code></td><td>Website is an invalid format.</td><td><p class="markdown-p">Website must be well-formed. The <code class="syntax-inline syntax-inline--theme">http://</code> at the beginning is optional. If you want to provide websites that may be not well-formed you can use <a href="/reference/request/customer/create/java#custom_fields"><code class="syntax-inline syntax-inline--theme">customFields()</code></a></p></td></tr>
  </tbody>
</table>

<h2 class="markdown-h2">
  Payment method
  <a class="icon icon--link hash-link" href="#payment-method">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="payment-method"></a>
</h2>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-93101" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93101</code></td><td>Payment method params are required.</td><td><p class="markdown-p">A top level payment method parameter is missing.</p></td></tr>
    <tr id="code-93102" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93102</code></td><td>Nonce is invalid.</td><td><p class="markdown-p">The nonce that was received is not a valid nonce.</p></td></tr>
    <tr id="code-93103" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93103</code></td><td>Nonce is required.</td><td><p class="markdown-p">A nonce was not provided.</p></td></tr>
    <tr id="code-93104" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93104</code></td><td>Customer ID is required.</td><td><p class="markdown-p">A customer id was not provided.</p></td></tr>
    <tr id="code-93105" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93105</code></td><td>Customer ID is invalid.</td><td><p class="markdown-p">The customer id does not reference a customer.</p></td></tr>
    <tr id="code-93106" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93106</code></td><td>Cannot forward a payment method of this type.</td><td><p class="markdown-p">Only credit cards may be forwarded.</p></td></tr>
    <tr id="code-93107" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93107</code></td><td>Cannot use a payment_method_nonce more than once.</td><td><p class="markdown-p">A payment method nonce may only be consumed once.</p></td></tr>
    <tr id="code-93108" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93108</code></td><td>Unknown or expired payment_method_nonce.</td><td><p class="markdown-p">The <a href="/guides/payment-method-nonces">payment method nonce</a> has either expired or never existed. Nonces are deleted upon expiration (3 hours after generation).</p></td></tr>
    <tr id="code-93109" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93109</code></td><td>Nonce is not vaultable.</td><td><p class="markdown-p">Nonce is not vaultable.</p></td></tr>



    <tr id="code-93113" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93113</code></td><td>PayPal custom field must be less than 256 characters in length.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-93114" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93114</code></td><td>PayPal description must be less than 256 characters in length.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-93115" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93115</code></td><td>Order ID must be less than 256 characters in length.</td><td><p class="markdown-p">Maximum 255 characters.</p></td></tr>
    <tr id="code-93116" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93116</code></td><td>Amount format is invalid.</td><td><p class="markdown-p">Amount must be formatted like &#39;10&#39; or &#39;10.00&#39;.</p></td></tr>
    <tr id="code-93117" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93117</code></td><td>This payment method is no longer supported.</td><td><p class="markdown-p">This payment method is no longer supported.</p></td></tr>
    <tr id="code-93118" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93118</code></td><td>PayPal refresh token is invalid.</td><td><p class="markdown-p">PayPal has reported this refresh token is invalid.</p></td></tr>
    <tr id="code-93119" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93119</code></td><td>Nonce is not a valid parameter when PayPal refresh token is provided.</td><td><p class="markdown-p">Nonce is not a valid parameter when PayPal refresh token is provided.</p></td></tr>
    <tr id="code-93120" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93120</code></td><td>PayPal merchant account required to vault refresh token.</td><td><p class="markdown-p">A PayPal merchant account required to vault a refresh token. Enable PayPal in a new or existing merchant account and retry.</p></td></tr>
    <tr id="code-93121" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93121</code></td><td>US bank account verification method is invalid.</td><td><p class="markdown-p">Valid US bank account verification methods include &#39;independent_check&#39; or &#39;network_check&#39;.</p></td></tr>
    <tr id="code-93122" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93122</code></td><td>US bank account is not accepted by merchant account.</td><td><p class="markdown-p">A merchant account must support US bank accounts before a US bank account payment method can be created.</p></td></tr>
  </tbody>
</table>

<h3 class="markdown-h3">
  Apple Pay
  <a class="icon icon--link hash-link" href="#apple-pay">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="apple-pay"></a>
</h3>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-83501" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">83501</code></td><td>Apple Pay cards are not accepted by this merchant account.</td><td><p class="markdown-p">Apple Pay cards are not accepted by this merchant account.</p></td></tr>
    <tr id="code-83502" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">83502</code></td><td>A customer ID is required to vault an Apple Pay Card.</td><td><p class="markdown-p">When storing an Apple Pay card in the vault, you must provide the customer ID of a customer already stored in the vault to whom the card will belong.</p></td></tr>
    <tr id="code-93503" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93503</code></td><td>Apple Pay token is taken.</td><td><p class="markdown-p">Payment method tokens must be unique across all payment method types.</p></td></tr>
    <tr id="code-93504" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93504</code></td><td>Cannot use a payment_method_nonce more than once.</td><td><p class="markdown-p">The <a href="/guides/payment-method-nonces">payment method nonce</a> has already been used.</p></td></tr>
    <tr id="code-93505" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93505</code></td><td>Unknown or expired payment_method_nonce.</td><td><p class="markdown-p">The <a href="/guides/payment-method-nonces">payment method nonce</a> has either expired or never existed. Nonces are deleted upon expiration (3 hours after generation).</p></td></tr>
    <tr id="code-93506" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93506</code></td><td>Payment method nonce locked.</td><td><p class="markdown-p"><strong>Deprecated</strong><br/> The <a href="/guides/payment-method-nonces">payment method nonce</a> must be unlocked before it is used.</p></td></tr>
    <tr id="code-83518" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">83518</code></td><td>Credit card type is not accepted by this merchant account.</td><td><p class="markdown-p">The specified merchant account is not configured to accept cards from this payment network. Please specify the correct payment networks when initializing a PKPaymentRequest.</p></td></tr>
    <tr id="code-93507" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93507</code></td><td>Payment method nonces cannot be used to update an existing Apple Pay Card.</td><td><p class="markdown-p">A vaulted payment method cannot be updated with an Apple Pay nonce. Create a new payment method instead.</p></td></tr>
    <tr id="code-93508" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93508</code></td><td>Number is required for Apple Pay Card</td><td><p class="markdown-p">The Apple Pay <code class="syntax-inline syntax-inline--theme">PKPaymentToken</code> payment data was malformed (did not contain a card number).</p></td></tr>
    <tr id="code-93509" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93509</code></td><td>Expiration Month is required for Apple Pay Card</td><td><p class="markdown-p">The Apple Pay <code class="syntax-inline syntax-inline--theme">PKPaymentToken</code> payment data was malformed (did not contain an expiration month).</p></td></tr>
    <tr id="code-93510" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93510</code></td><td>Expiration Year is required for Apple Pay Card</td><td><p class="markdown-p">The Apple Pay <code class="syntax-inline syntax-inline--theme">PKPaymentToken</code> payment data was malformed (did not contain an expiration year).</p></td></tr>
    <tr id="code-93511" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93511</code></td><td>Cryptogram is required for Apple Pay Card</td><td><p class="markdown-p">The Apple Pay <code class="syntax-inline syntax-inline--theme">PKPaymentToken</code> payment data was malformed (did not contain a cryptogram). This is sometimes caused by misconfigured <code class="syntax-inline syntax-inline--theme">merchantCapabilities</code> in the <code class="syntax-inline syntax-inline--theme">PKPaymentRequest</code>. See <a href="/guides/apple-pay/client-side#create-a-pkpaymentrequest">our recommendations</a> in the Apple Pay guide.</p></td></tr>
    <tr id="code-83512" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">83512</code></td><td>Apple Pay payment data decryption failed</td><td><p class="markdown-p">The Apple Pay <code class="syntax-inline syntax-inline--theme">PKPaymentToken</code> payment data could not be decrypted. This occurs when (a) the Apple Pay merchant id used in your iOS App entitlements does not match the values provided to Braintree; (b) the provisioning profile you used to sign your iOS App does not correspond to the iOS Developer Account with which the Apple Pay certificate was generated; (c) the payment data was not valid as it was received by the Gateway. <a href="/forms/contact">Contact our Support team</a> if you cannot resolve this error.</p></td></tr>
    <tr id="code-93513" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93513</code></td><td>Apple Pay is disabled for this merchant</td><td><p class="markdown-p">Your merchant account is not configured for Apple Pay support. <a href="/forms/contact">Contact our Support team</a> to configure and enable Apple Pay.</p></td></tr>
    <tr id="code-93514" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93514</code></td><td>Apple Pay certificate, private key or merchant ID not configured</td><td><p class="markdown-p">Your merchant account is not configured for Apple Pay support. <a href="/forms/contact">Contact our Support team</a> to configure and enable Apple Pay.</p></td></tr>
    <tr id="code-93517" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93517</code></td><td>Certificate provided is not valid</td><td><p class="markdown-p">Certificate provided is not valid.</p></td></tr>
    <tr id="code-93519" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93519</code></td><td>Public key used to sign payment data does not match stored certificate</td><td><p class="markdown-p">Public key used to sign payment data does not match stored certificate.</p></td></tr>
    <tr id="code-83520" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">83520</code></td><td>Payment data is malformed</td><td><p class="markdown-p">Payment data is malformed.</p></td></tr>
    <tr id="code-93521" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93521</code></td><td>Private key stored does not match private key used to encrypt payment data</td><td><p class="markdown-p">Private key stored does not match private key used to encrypt payment data.</p></td></tr>
    <tr id="code-93522" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93522</code></td><td>Certificate does not match stored key pair</td><td><p class="markdown-p">The Apple Pay certificate you uploaded does not match the key pair we have stored for your account. Please download a new CSR from the Control Panel and create a new certificate for your Apple Pay merchant ID using this CSR.</p></td></tr>
    <tr id="code-93523" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93523</code></td><td>Domain name is required.</td><td><p class="markdown-p">You must specify a domain name.</p></td></tr>
    <tr id="code-93524" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93524</code></td><td>An error occurred when validating your domain with Apple.</td><td><p class="markdown-p">An error occurred when validating your domain with Apple. Please try again.</p></td></tr>
    <tr id="code-93525" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93525</code></td><td>Domain verification with Apple failed. Please verify the file is available at the verification path and try again.</td><td><p class="markdown-p">Domain verification with Apple failed. Please verify the file is available at the verification path and try again.</p></td></tr>
    <tr id="code-93526" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93526</code></td><td>There was an issue contacting Apple, please try again later.</td><td><p class="markdown-p">There was an issue contacting Apple, please try again later.</p></td></tr>
  </tbody>
</table>

<h3 class="markdown-h3">
  Credit card
  <a class="icon icon--link hash-link" href="#credit-card">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="credit-card"></a>
</h3>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-91701" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91701</code></td><td>Cannot provide both a billing address and a billing address ID.</td><td><p class="markdown-p">When you create or update a credit card you can set the billing address using full billing address details, or you can set it to a billing address ID of an address already associated to the customer, but not both.</p></td></tr>
    <tr id="code-91702" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91702</code></td><td>Billing address ID is invalid.</td><td><p class="markdown-p">If setting the billing address on a credit card using an ID, the ID must be an ID of an address associated to the customer.</p></td></tr>
    <tr id="code-91704" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91704</code></td><td>Customer ID is required.</td><td><p class="markdown-p">When adding a credit card to an existing customer, the customer ID is required.</p></td></tr>
    <tr id="code-91705" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91705</code></td><td>Customer ID is invalid.</td><td><p class="markdown-p">When specifying the customer ID to add a credit card to an existing customer, the ID must be the ID a customer stored in the Vault.</p></td></tr>
    <tr id="code-91708" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91708</code></td><td>Cannot provide expiration<em>date if you are also providing expiration_month and expiration_year.</td><td><p class="markdown-p">You can provide the credit card expiration date as a single field, or as month and year separately, but not all 3.</p></td></tr>
    <tr id="code-91718" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91718</code></td><td>Token is invalid (use only letters, numbers, &#39;-&#39;, and &#39;</em>&#39;).</td><td><p class="markdown-p">If you&#39;re specifying the credit card token, you can use letters, numbers, &#39;-&#39;, and &#39;_&#39;.</p></td></tr>
    <tr id="code-91719" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91719</code></td><td>Credit card token is taken.</td><td><p class="markdown-p">Credit card tokens have to be unique.</p></td></tr>
    <tr id="code-91720" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91720</code></td><td>Credit card token is too long.</td><td><p class="markdown-p">Maximum 36 characters.</p></td></tr>
    <tr id="code-91721" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91721</code></td><td>Token is not an allowed token.</td><td><p class="markdown-p">We reserve a few tokens: &#39;new&#39; and &#39;all&#39;.</p></td></tr>
    <tr id="code-91722" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91722</code></td><td>Payment Method token is required.</td><td><p class="markdown-p">When updating a credit card you can omit the token if you don&#39;t want to change it, but you can&#39;t set it to an empty string. If set to an empty string on creation, the gateway will generate a random token.</p></td></tr>
    <tr id="code-91744" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91744</code></td><td>Billing address format is invalid.</td><td><p class="markdown-p">Billing address format is invalid.</p></td></tr>



    <tr id="code-81723" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81723</code></td><td>Cardholder name is too long.</td><td><p class="markdown-p">Maximum 175 characters.</p></td></tr>
    <tr id="code-81703" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81703</code></td><td>Credit card type is not accepted by this merchant account.</td><td><p class="markdown-p">Applies when specifying a credit card in a sale or verification request. Not applicable when only storing in the Vault, since Vault records are not associated to specific merchant accounts.</p></td></tr>
    <tr id="code-81718" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81718</code></td><td>Credit card number cannot be updated to an unsupported card type when it is associated to subscriptions.</td><td><p class="markdown-p">Only applies when using recurring billing. If a credit card is being used for recurring billing subscriptions, the card can only be updated to a card type that is accepted by the merchant account that is being used for the subscriptions.</p></td></tr>
    <tr id="code-81706" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81706</code></td><td>CVV is required.</td><td><p class="markdown-p">CVV will only be required if CVV processing rules are configured to require it. If the rules are configured to require it, then CVV is required when storing a card in the Vault and performing card verification or when creating transactions.</p></td></tr>
    <tr id="code-81707" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81707</code></td><td>CVV must be 4 digits for American Express and 3 digits for other card types.</td><td><p class="markdown-p">CVV must be 4 digits for American Express and 3 digits for other card types.</p></td></tr>
    <tr id="code-81709" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81709</code></td><td>Expiration date is required.</td><td><p class="markdown-p">You must provide the expiration date either as a single field or as month and year separately.</p></td></tr>
    <tr id="code-81710" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81710</code></td><td>Expiration date is invalid.</td><td><p class="markdown-p">Valid formats are M/YY, M/YYYY, MM/YY, and MM/YYYY. The month must be 1-12 or 01-12.</p></td></tr>
    <tr id="code-81711" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81711</code></td><td>Expiration year is invalid. It must be between 1975 and 2201.</td><td><p class="markdown-p">The expiration year must be greater than 1975 and less than 2201.</p></td></tr>
    <tr id="code-81712" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81712</code></td><td>Expiration month is invalid.</td><td><p class="markdown-p">It must be 1-12 or 01-12.</p></td></tr>
    <tr id="code-81713" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81713</code></td><td>Expiration year is invalid.</td><td><p class="markdown-p">It must be between 1975 and 2201.</p></td></tr>
    <tr id="code-81714" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81714</code></td><td>Credit card number is required.</td><td><p class="markdown-p">You&#39;ll get this error if number is omitted or if it is an empty string.</p></td></tr>
    <tr id="code-81715" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81715</code></td><td>Credit card number is invalid.</td><td><p class="markdown-p">The credit card number must pass a Luhn-10 check.</p></td></tr>
    <tr id="code-81716" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81716</code></td><td>Credit card number must be 12-19 digits.</td><td><p class="markdown-p">Inclusive.</p></td></tr>
    <tr id="code-81717" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81717</code></td><td>Credit card number is not an accepted test number.</td><td><p class="markdown-p">Only <a href="/reference/general/testing#credit-card-numbers">test numbers</a> can be used in the sandbox.</p></td></tr>
    <tr id="code-91723" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91723</code></td><td>Update Existing Token is invalid.</td><td><p class="markdown-p">Applies when <a href="/reference/request/customer/update#update-customer-and-existing-credit-card">updating a customer and credit card</a> at the same time and specifying the token of the credit card to update. You&#39;ll get this error if the token specified is for a credit card that does not exist, or references a credit card that does not belong to the customer that is being updated.</p></td></tr>
    <tr id="code-81724" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81724</code></td><td>Duplicate card exists in the vault.</td><td><p class="markdown-p">Duplicate card exists in the vault.</p></td></tr>
    <tr id="code-81725" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81725</code></td><td>Credit card must include number, payment_method_nonce, or venmo_sdk_payment_method_code.</td><td><p class="markdown-p">Credit card must include number, payment_method_nonce, or venmo_sdk_payment_method_code.</p></td></tr>
    <tr id="code-91726" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91726</code></td><td>Credit card type is not accepted by this merchant account.</td><td><p class="markdown-p">Credit card type is not accepted by this merchant account.</p></td></tr>
    <tr id="code-91727" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91727</code></td><td>Invalid VenmoSDK payment method code</td><td><p class="markdown-p">Invalid VenmoSDK payment method code.</p></td></tr>
    <tr id="code-91728" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91728</code></td><td>Verification Merchant Account ID is invalid.</td><td><p class="markdown-p">There must be a merchant account with this ID.</p></td></tr>
    <tr id="code-91729" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91729</code></td><td>Update Existing Token is not allowed when creating a customer.</td><td><p class="markdown-p">Update Existing Token is not allowed when creating a customer.</p></td></tr>
    <tr id="code-91730" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91730</code></td><td>Verifications are not supported on this merchant account</td><td><p class="markdown-p">This error occurs when a merchant account does not support credit card verification. This can also occur if your <a href="https://articles.braintreepayments.com/control-panel/important-gateway-credentials#api-credentials">API user</a> does not have access to the merchant account used for the verification.</p></td></tr>
    <tr id="code-91731" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91731</code></td><td>Cannot use a payment_method_nonce more than once.</td><td><p class="markdown-p">The <a href="/guides/payment-method-nonces">payment method nonce</a> has already been used once.</p></td></tr>
    <tr id="code-91732" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91732</code></td><td>Unknown or expired payment_method_nonce.</td><td><p class="markdown-p">The <a href="/guides/payment-method-nonces">payment method nonce</a> has either expired or never existed. Nonces are deleted upon expiration (3 hours after generation).</p></td></tr>
    <tr id="code-91733" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91733</code></td><td>Payment method nonce locked.</td><td><p class="markdown-p"><strong>Deprecated</strong><br/>The <a href="/guides/payment-method-nonces">payment method nonce</a> must be unlocked before it is used.</p></td></tr>
    <tr id="code-91734" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91734</code></td><td>Credit card type is not accepted by this merchant account.</td><td><p class="markdown-p">Applies when specifying a credit card when creating a transaction, but not when only storing in the Vault since Vault records are not associated to specific merchant accounts.</p></td></tr>
    <tr id="code-91735" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91735</code></td><td>Payment method nonces cannot be used to update an existing card.</td><td><p class="markdown-p">A <a href="/guides/payment-method-nonces">payment method nonce</a> cannot be used to update an existing credit card.</p></td></tr>
    <tr id="code-91738" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91738</code></td><td>Payment method is not a credit card payment method.</td><td><p class="markdown-p">This operation requires a credit card, and the payment method you specified is not a credit card.</p></td></tr>
    <tr id="code-91742" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91742</code></td><td>Verification Merchant Account is suspended.</td><td><p class="markdown-p">Verification Merchant Account is suspended.</p></td></tr>
    <tr id="code-91743" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91743</code></td><td>The current user does not have access to the specified verification_merchant_account_id</td><td><p class="markdown-p">The current user does not have access to the specified verification_merchant_account_id.</p></td></tr>
    <tr id="code-81736" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81736</code></td><td>CVV verification failed.</td><td><p class="markdown-p">CVV was incorrect or not supplied.</p></td></tr>
    <tr id="code-81737" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81737</code></td><td>Postal code verification failed.</td><td><p class="markdown-p">Postal code was incorrect or not supplied.</p></td></tr>
    <tr id="code-91739" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91739</code></td><td>Verification amount cannot be negative.</td><td><p class="markdown-p">The amount you specified for verification was less than zero.</p></td></tr>
    <tr id="code-91740" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91740</code></td><td>Verification amount is invalid.</td><td><p class="markdown-p">The amount you specified for verification had an invalid format.</p></td></tr>
    <tr id="code-91741" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91741</code></td><td>Verification amount not supported by processor.</td><td><p class="markdown-p">The processor you are using for verification does not allow the verification amount you specified.</p></td></tr>
    <tr id="code-91745" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91745</code></td><td>Payment method params supplied are not valid for updating a credit card.</td><td><p class="markdown-p">The payment method params you supplied are not valid for updating a credit card.</p></td></tr>

    <tr id="code-81750" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81750</code></td><td>Credit card number is prohibited.</td><td><p class="markdown-p">Cannot transact with an issuer on OFAC&#39;s prohibited list.</p></td></tr>

    <tr id="code-91752" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91752</code></td><td>Verification amount is too large.</td><td><p class="markdown-p">Verification amount is too large.</p></td></tr>

    <tr id="code-91755" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91755</code></td><td>Verification Merchant Account ID cannot be a sub-merchant account.</td><td><p class="markdown-p">Verifications cannot be created using sub-merchant accounts.</p></td></tr>
    <tr id="code-91756" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91756</code></td><td>Customer ID cannot be updated.</td><td><p class="markdown-p">Customer ID cannot be updated.</p></td></tr>
  </tbody>
</table>

<h4 class="markdown-h4">
  American Express industry data
  <a class="icon icon--link hash-link" href="#american-express-industry-data">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="american-express-industry-data"></a>
</h4>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-93401" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93401</code></td><td>Industry type is invalid.</td><td><p class="markdown-p">Industry type is invalid.</p></td></tr>
    <tr id="code-93402" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93402</code></td><td>Lodging data is empty.</td><td><p class="markdown-p">Lodging data is empty.</p></td></tr>
    <tr id="code-93403" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93403</code></td><td>Folio number is invalid.</td><td><p class="markdown-p">Folio number is invalid.</p></td></tr>
    <tr id="code-93404" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93404</code></td><td>Check in date is invalid.</td><td><p class="markdown-p">Check in date is invalid.</p></td></tr>
    <tr id="code-93405" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93405</code></td><td>Check out date is invalid.</td><td><p class="markdown-p">Check out date is invalid.</p></td></tr>
    <tr id="code-93406" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93406</code></td><td>Check out date must occur during or after the check in date.</td><td><p class="markdown-p">Check out date must occur during or after the check in date.</p></td></tr>
    <tr id="code-93407" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93407</code></td><td>Data fields are unknown.</td><td><p class="markdown-p">Data fields are unknown.</p></td></tr>
    <tr id="code-93408" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93408</code></td><td>Travel and Cruise data is empty.</td><td><p class="markdown-p">Travel and Cruise data is empty.</p></td></tr>
    <tr id="code-93409" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93409</code></td><td>Data fields are unknown.</td><td><p class="markdown-p">Data fields are unknown.</p></td></tr>
    <tr id="code-93410" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93410</code></td><td>Travel Package is invalid.</td><td><p class="markdown-p">Travel Package is invalid.</p></td></tr>
    <tr id="code-93411" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93411</code></td><td>Departure date is invalid.</td><td><p class="markdown-p">Departure date is invalid.</p></td></tr>
    <tr id="code-93412" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93412</code></td><td>Lodging check in date is invalid.</td><td><p class="markdown-p">Lodging check in date is invalid.</p></td></tr>
    <tr id="code-93413" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">93413</code></td><td>Lodging check out date is invalid.</td><td><p class="markdown-p">Lodging check out date is invalid.</p></td></tr>
  </tbody>
</table>


<h3 class="markdown-h3">
  PayPal
  <a class="icon icon--link hash-link" href="#paypal">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="paypal"></a>
</h3>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-82901" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82901</code></td><td>Incomplete PayPal account information.</td><td><p class="markdown-p">You must specify an access token or a consent code for this operation.</p></td></tr>
    <tr id="code-82902" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82902</code></td><td>Pre-Approved Payment enabled PayPal account required for vaulting.</td><td><p class="markdown-p">When you vault a PayPal account, you must provide a <a href="/guides/payment-method-nonces">payment method nonce</a> that was retrieved via the <a href="/guides/paypal/vault">Vault flow</a>.</p></td></tr>
    <tr id="code-82903" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82903</code></td><td>Invalid PayPal account information.</td><td><p class="markdown-p">You cannot specify both an access token and a consent code for this operation.</p></td></tr>
    <tr id="code-82904" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82904</code></td><td>PayPal Accounts are not accepted by this merchant account.</td><td><p class="markdown-p">Your account has not been enabled to accept PayPal.</p></td></tr>
    <tr id="code-82905" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82905</code></td><td>A customer ID is required to vault a PayPal Account.</td><td><p class="markdown-p">When adding a PayPal account to an existing customer, the customer ID is required.</p></td></tr>
    <tr id="code-92906" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92906</code></td><td>PayPal Account token is taken.</td><td><p class="markdown-p">PayPal account tokens have to be unique.</p></td></tr>
    <tr id="code-92907" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92907</code></td><td>Cannot use a payment_method_nonce more than once.</td><td><p class="markdown-p">A payment method nonce may only be consumed once.</p></td></tr>
    <tr id="code-92908" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92908</code></td><td>Unknown or expired payment_method_nonce.</td><td><p class="markdown-p">The <a href="/guides/payment-method-nonces">payment method nonce</a> has either expired or never existed. Nonces are deleted upon expiration (3 hours after generation).</p></td></tr>
    <tr id="code-92909" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92909</code></td><td>Payment method nonce locked.</td><td><p class="markdown-p"><strong>Deprecated</strong><br/> The <a href="/guides/payment-method-nonces">payment method nonce</a> must be unlocked before it is used.</p></td></tr>
    <tr id="code-92910" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92910</code></td><td>Error communicating with PayPal.</td><td><p class="markdown-p">There was an error communicating with PayPal.</p></td></tr>
    <tr id="code-92911" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92911</code></td><td>PayPal authentication expired.</td><td><p class="markdown-p"><strong>Deprecated</strong><br/> The authentication you received from your user has expired.</p></td></tr>
    <tr id="code-92912" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92912</code></td><td>Funding source selection was given without an access token.</td><td><p class="markdown-p">You cannot specify a funding source without also specifying an access token.</p></td></tr>
    <tr id="code-92913" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92913</code></td><td>Funding source object is invalid or missing required fields.</td><td><p class="markdown-p">You sent an invalid or incomplete funding source specification.</p></td></tr>
    <tr id="code-92914" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92914</code></td><td>Payment method nonces cannot be used to update an existing PayPal account.</td><td><p class="markdown-p">A <a href="/guides/payment-method-nonces">payment method nonce</a> cannot be used to update an existing PayPal account.</p></td></tr>
    <tr id="code-92915" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92915</code></td><td>Payment method params supplied are not valid for updating a PayPal account.</td><td><p class="markdown-p">The payment method params you supplied are not valid for updating a PayPal account.</p></td></tr>
    <tr id="code-92916" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92916</code></td><td>Error executing PayPal order.</td><td><p class="markdown-p">There was an error while executing the PayPal order.</p></td></tr>
    <tr id="code-92917" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92917</code></td><td>Error executing PayPal billing agreement.</td><td><p class="markdown-p">There was an error while executing the PayPal billing agreement.</p></td></tr>
    <tr id="code-92918" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92918</code></td><td>Merchant setup must be completed before vaulting PayPal payment methods.</td><td><p class="markdown-p">The merchant account used is not fully set up; PayPal payment methods cannot be vaulted until setup is completed.</p></td></tr>
    <tr id="code-92919" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92919</code></td><td>This merchant account does not allow PayPal payments using the old Vault flow.</td><td><p class="markdown-p">Your account does not have the old Vault flow enabled for PayPal payments. <a href="/forms/contact">Contact our Support team</a> to enable the old Vault flow.</p></td></tr>
    <tr id="code-92920" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92920</code></td><td>Using a payment method nonce for PayPal intent=order is not permitted.</td><td><p class="markdown-p">Create a payment method from the nonce and then use the payment method token in the transaction sale request.</p></td></tr>
  </tbody>
</table>



<h3 class="markdown-h3">
  Venmo
  <a class="icon icon--link hash-link" href="#venmo">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="venmo"></a>
</h3>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-84101" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">84101</code></td><td>Common ID is required.</td><td><p class="markdown-p">Common ID is required.</p></td></tr>
    <tr id="code-84102" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">84102</code></td><td>Username is required.</td><td><p class="markdown-p">Username is required.</p></td></tr>
    <tr id="code-84103" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">84103</code></td><td>Venmo user ID is required.</td><td><p class="markdown-p">Venmo user ID is required.</p></td></tr>
    <tr id="code-84104" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">84104</code></td><td>Customer ID is required.</td><td><p class="markdown-p">Customer ID is required.</p></td></tr>
    <tr id="code-84105" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">84105</code></td><td>Venmo accounts are not accepted by this merchant account.</td><td><p class="markdown-p">Venmo accounts are not accepted by this merchant account.</p></td></tr>
    <tr id="code-84106" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">84106</code></td><td>Customer ID is invalid.</td><td><p class="markdown-p">Customer ID is invalid.</p></td></tr>


  </tbody>
</table>





<h2 class="markdown-h2">
  Recurring billing
  <a class="icon icon--link hash-link" href="#recurring-billing">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="recurring-billing"></a>
</h2>
<h3 class="markdown-h3">
  Add-ons/Discounts
  <a class="icon icon--link hash-link" href="#add-ons/discounts">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="add-ons/discounts"></a>
</h3>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-92001" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92001</code></td><td>Quantity is invalid.</td><td><p class="markdown-p">Quantity must be a number.</p></td></tr>
    <tr id="code-92002" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92002</code></td><td>Amount is invalid.</td><td><p class="markdown-p">Amount must be formatted like &#39;10&#39; or &#39;10.00&#39;.</p></td></tr>
    <tr id="code-92003" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92003</code></td><td>Amount cannot be blank.</td><td><p class="markdown-p">Blanks are not allowed.</p></td></tr>
    <tr id="code-92004" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92004</code></td><td>Quantity cannot be blank.</td><td><p class="markdown-p">Blanks are not allowed.</p></td></tr>
    <tr id="code-92005" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92005</code></td><td>Number of billing cycles is invalid.</td><td><p class="markdown-p">Number of billing cycles must be numeric.</p></td></tr>
    <tr id="code-92010" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92010</code></td><td>Quantity must be greater than zero.</td><td><p class="markdown-p">Quantity must be greater than 0.</p></td></tr>
    <tr id="code-92011" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92011</code></td><td>Existing ID is invalid.</td><td><p class="markdown-p">Modification ID must be associated with the subscription.</p></td></tr>
    <tr id="code-92012" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92012</code></td><td>Existing ID is required.</td><td><p class="markdown-p">Modification ID is required to update a modification.</p></td></tr>
    <tr id="code-92013" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92013</code></td><td>Inherited From ID is invalid.</td><td><p class="markdown-p">Modification with that inherited from ID is not available.</p></td></tr>
    <tr id="code-92014" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92014</code></td><td>Inherited From ID is required.</td><td><p class="markdown-p">Must provide an inherited from ID.</p></td></tr>
    <tr id="code-92015" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92015</code></td><td>Cannot update a removed add-on or discount.</td><td><p class="markdown-p">Cannot update and remove a modification at the same time.</p></td></tr>
    <tr id="code-92016" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92016</code></td><td>Cannot remove add-on or discount if not already associated with subscription.</td><td><p class="markdown-p">Cannot remove add-on or discount if not already associated with subscription.</p></td></tr>
    <tr id="code-92017" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92017</code></td><td>Number of billing cycles cannot be blank.</td><td><p class="markdown-p">Number Of Billing Cycles cannot be blank if the subscription expires.</p></td></tr>
    <tr id="code-92018" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92018</code></td><td>Cannot specify both number of billing cycles and never expires as true.</td><td><p class="markdown-p">Number of billing cycles is blank and never expires is not set to true.</p></td></tr>
    <tr id="code-92019" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92019</code></td><td>Number of billing cycles must be greater than zero.</td><td><p class="markdown-p">Number of billing cycles must be greater than 0.</p></td></tr>
    <tr id="code-92020" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92020</code></td><td>Existing ID is not of the correct kind.</td><td><p class="markdown-p">Existing ID must be of the type of modification that is being edited.</p></td></tr>
    <tr id="code-92021" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92021</code></td><td>ID to remove is incorrect kind.</td><td><p class="markdown-p">Existing ID must be of the type of modification that is being removed.</p></td></tr>
    <tr id="code-92022" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92022</code></td><td>Cannot edit add-on or discount on a past due subscription.</td><td><p class="markdown-p">Unable to edit modifications on subscriptions that are past due.</p></td></tr>
    <tr id="code-92023" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92023</code></td><td>Amount is too large.</td><td><p class="markdown-p">The amount cannot be greater than the maximum allowed by the processor. <a href="/forms/contact">Contact our Support team</a> for your specific limit.</p></td></tr>
    <tr id="code-92024" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92024</code></td><td>Cannot pass null modification.</td><td><p class="markdown-p">Modification is missing from the API call.</p></td></tr>
    <tr id="code-92025" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92025</code></td><td>ID to remove is invalid.</td><td><p class="markdown-p">ID to remove is invalid.</p></td></tr>
  </tbody>
</table>

<h3 class="markdown-h3">
  Subscription
  <a class="icon icon--link hash-link" href="#subscription">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="subscription"></a>
</h3>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-81901" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81901</code></td><td>Cannot edit a canceled subscription.</td><td><p class="markdown-p">After a subscription has been canceled it cannot be updated.</p></td></tr>
    <tr id="code-81902" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81902</code></td><td>ID has already been taken.</td><td><p class="markdown-p">Subscription IDs need to be unique.</p></td></tr>
    <tr id="code-81903" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81903</code></td><td>Price cannot be blank.</td><td><p class="markdown-p">If you provide a price, it can&#39;t be an empty string. If you omit the price, then the subscription will inherit the price from the plan.</p></td></tr>
    <tr id="code-81904" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81904</code></td><td>Price is an invalid format.</td><td><p class="markdown-p">Price must be formatted like &#39;10&#39; or &#39;10.00&#39;.</p></td></tr>
    <tr id="code-81905" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81905</code></td><td>Subscription has already been canceled.</td><td><p class="markdown-p">You can&#39;t cancel subscriptions that have already been canceled.</p></td></tr>
    <tr id="code-81906" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81906</code></td><td>ID is invalid (use only letters, numbers, &#39;-&#39;, and &#39;<em>&#39;).</td><td><p class="markdown-p">If specifying the ID for the subscription, you can only use letters, numbers, </em> and -.</p></td></tr>
    <tr id="code-81907" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81907</code></td><td>Trial Duration is an invalid format.</td><td><p class="markdown-p">It must be 1-3 digits.</p></td></tr>
    <tr id="code-81908" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81908</code></td><td>Trial Duration is required.</td><td><p class="markdown-p">It&#39;s required if trial period is set to true.</p></td></tr>
    <tr id="code-81909" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81909</code></td><td>Trial Duration Unit is invalid.</td><td><p class="markdown-p">Valid values are &quot;day&quot; and &quot;month&quot;.</p></td></tr>
    <tr id="code-81910" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81910</code></td><td>Cannot edit an expired subscription.</td><td><p class="markdown-p">You cannot edit a subscription with Expired status.</p></td></tr>
    <tr id="code-81923" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81923</code></td><td>Price is too large.</td><td><p class="markdown-p">The subscription price cannot be greater than the maximum allowed by the processor. <a href="/forms/contact">Contact our Support team</a> for your specific limit.</p></td></tr>
    <tr id="code-91901" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91901</code></td><td>Merchant Account ID is invalid.</td><td><p class="markdown-p">If specifying the merchant account to use to process transactions for this subscription it needs to be the ID for one of your merchant accounts.</p></td></tr>
    <tr id="code-91902" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91902</code></td><td>Payment method token payment instrument type is not accepted by this merchant account.</td><td><p class="markdown-p">When providing a payment method token, your merchant account must be configured to accept the payment method type represented by the token.</p></td></tr>
    <tr id="code-91903" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91903</code></td><td>Payment method token is invalid.</td><td><p class="markdown-p">You&#39;ll get this error if we can&#39;t find a payment method with the token specified.</p></td></tr>
    <tr id="code-91904" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91904</code></td><td>Plan ID is invalid.</td><td><p class="markdown-p">You&#39;ll get this error if we can&#39;t find a plan with the given ID.</p></td></tr>
    <tr id="code-91905" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91905</code></td><td>Payment method token does not belong to the subscription&#39;s customer.</td><td><p class="markdown-p">When updating a subscription and changing the payment method token, you can only use tokens associated to the same customer that the subscription is currently associated to.</p></td></tr>
    <tr id="code-91906" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91906</code></td><td>Number Of Billing Cycles must be numeric.</td><td><p class="markdown-p">It must be a number.</p></td></tr>
    <tr id="code-91907" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91907</code></td><td>Number Of Billing Cycles must be greater than zero.</td><td><p class="markdown-p">It must be greater than 0.</p></td></tr>
    <tr id="code-91908" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91908</code></td><td>Cannot specify both number of billing cycles and never expires as true.</td><td><p class="markdown-p">You cannot specify both number of billing cycles and never expires as true.</p></td></tr>
    <tr id="code-91909" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91909</code></td><td>Number Of Billing Cycles is less than the current billing cycle.</td><td><p class="markdown-p">You cannot edit a subscription and change the number of billing cycles to be below the current count of billing cycles.</p></td></tr>
    <tr id="code-91911" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91911</code></td><td>Cannot add duplicate add-on or discount.</td><td><p class="markdown-p">Add-Ons and Discounts must be unique, but you can change the quantity.</p></td></tr>
    <tr id="code-91912" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91912</code></td><td>Number Of Billing Cycles cannot be blank if the subscription expires.</td><td><p class="markdown-p">Blanks are not allowed.</p></td></tr>
    <tr id="code-91913" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91913</code></td><td>Billing Day of Month must be numeric.</td><td><p class="markdown-p">The billing date must be a number.</p></td></tr>
    <tr id="code-91914" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91914</code></td><td>Billing Day of Month must be between 1 and 28, or 31.</td><td><p class="markdown-p">The billing date must be 1-28 or 31 (for the last day of every month).</p></td></tr>
    <tr id="code-91915" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91915</code></td><td>First Billing Date is invalid.</td><td><p class="markdown-p">The first billing date is an incorrect format.</p></td></tr>
    <tr id="code-91916" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91916</code></td><td>First Billing Date cannot be in the past.</td><td><p class="markdown-p">The first billing date cannot be in the past.</p></td></tr>
    <tr id="code-91917" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91917</code></td><td>Cannot specify more than one type of start date.</td><td><p class="markdown-p">The type of start date can be only one of the following: start immediately, after a trial period, or on a specific day of the month.</p></td></tr>
    <tr id="code-91918" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91918</code></td><td>Billing Day of Month cannot be updated.</td><td><p class="markdown-p">The billing date cannot be updated.</p></td></tr>
    <tr id="code-91919" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91919</code></td><td>First Billing Date cannot be updated.</td><td><p class="markdown-p">First billing date cannot be updated.</p></td></tr>
    <tr id="code-91920" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91920</code></td><td>Can only edit id, merchant account id, payment method token, and descriptor on a past due subscription.</td><td><p class="markdown-p">You cannot edit any fields which could change the price on a past due subscription.</p></td></tr>
    <tr id="code-91921" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91921</code></td><td>Invalid request format.</td><td><p class="markdown-p">The add-ons and discounts are in an invalid format.</p></td></tr>
    <tr id="code-91922" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91922</code></td><td>Cannot update subscription to a plan with a different billing frequency.</td><td><p class="markdown-p">You will get this validation if you try to update the plan on a subscription and the billing cycle for the new plan is not the same as the billing cycle of the old plan.</p></td></tr>
    <tr id="code-91923" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91923</code></td><td>Subscription Plan currency must be the same as the merchant account&#39;s currency.</td><td><p class="markdown-p">Subscription Plan currency must be the same as the merchant account&#39;s currency.</p></td></tr>
    <tr id="code-91924" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91924</code></td><td>Payment method nonce payment instrument type is not accepted by this merchant account.</td><td><p class="markdown-p">The supplied payment method nonce represents a payment method of a type that is not accepted by this merchant account.</p></td></tr>
    <tr id="code-91925" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91925</code></td><td>Payment method nonce is invalid.</td><td><p class="markdown-p">The supplied payment method nonce was not in a valid format or is unknown.</p></td></tr>
    <tr id="code-91926" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91926</code></td><td>Payment method nonce does not belong to the subscription&#39;s customer.</td><td><p class="markdown-p">The payment method nonce used to create a subscription must be vaulted and must belong to the customer owning the subscription.</p></td></tr>
    <tr id="code-91927" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91927</code></td><td>Payment method nonce represents an un-vaulted payment instrument.</td><td><p class="markdown-p">You cannot create a subscription with a nonce representing an unvaulted payment instrument. Use the payment method nonce to create a vaulted payment method first.</p></td></tr>
    <tr id="code-91928" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91928</code></td><td>Payment instrument type is not valid for subscriptions.</td><td><p class="markdown-p">Payment instrument type is not valid for subscriptions.</p></td></tr>
    <tr id="code-91929" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91929</code></td><td>Payment instrument type is not valid for subscriptions.</td><td><p class="markdown-p">Payment instrument type is not valid for subscriptions.</p></td></tr>
    <tr id="code-91930" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91930</code></td><td>Merchant Account does not support the given payment instrument type.</td><td><p class="markdown-p">Merchant Account does not support the given payment instrument type.</p></td></tr>
    <tr id="code-91931" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91931</code></td><td>Too many concurrent attempts to update this subscription. Try again later.</td><td><p class="markdown-p">Too many concurrent attempts to update this subscription. Try again later.</p></td></tr>
  </tbody>
</table>

<h2 class="markdown-h2">
  Search
  <a class="icon icon--link hash-link" href="#search">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="search"></a>
</h2>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-82301" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82301</code></td><td>Settlement Date is required</td><td><p class="markdown-p">You must provide a settlement date as the first argument.</p></td></tr>
    <tr id="code-82302" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82302</code></td><td>Settlement Date is invalid</td><td><p class="markdown-p">The settlement date provided must be a valid date.</p></td></tr>
    <tr id="code-82303" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">82303</code></td><td>Group By Custom Field is not a valid custom field</td><td><p class="markdown-p">The custom field provided must be valid.</p></td></tr>
  </tbody>
</table>

<h2 class="markdown-h2">
  Transaction
  <a class="icon icon--link hash-link" href="#transaction">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="transaction"></a>
</h2>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-81501" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81501</code></td><td>Amount cannot be negative.</td><td><p class="markdown-p">Even if creating a credit transaction, the amount should be given as x.xx, not -x.xx.</p></td></tr>
    <tr id="code-81502" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81502</code></td><td>Amount is required.</td><td><p class="markdown-p">You&#39;ll get this error if amount is not given or is blank.</p></td></tr>
    <tr id="code-81503" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81503</code></td><td>Amount is an invalid format.</td><td><p class="markdown-p">Amount must be formatted like &#39;10&#39; or &#39;10.00&#39;. If the <a href="/reference/general/currencies">currency does not use decimal places</a>, the amount cannot include decimal places.</p></td></tr>
    <tr id="code-81528" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81528</code></td><td>Amount is too large.</td><td><p class="markdown-p">The amount cannot be greater than the maximum allowed by the processor. <a href="/forms/contact">Contact our Support team</a> for your specific limit.</p></td></tr>
    <tr id="code-81509" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81509</code></td><td>Credit card type is not accepted by this merchant account.</td><td><p class="markdown-p">The credit card card type must be accepted by your merchant account. Note that there is a different error code when you get this error when creating transactions using tokens (<code class="syntax-inline syntax-inline--theme">91517</code>).</p></td></tr>
    <tr id="code-81527" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81527</code></td><td>Custom field is too long: </td><td><p class="markdown-p">Custom field values must be less than 255 characters. The error message for this validation error will contain a list of the custom fields that were too long.</p></td></tr>
    <tr id="code-91501" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91501</code></td><td>Order ID is too long.</td><td><p class="markdown-p">Order ID must be less than 255 characters.</p></td></tr>
    <tr id="code-91530" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91530</code></td><td>Cannot provide a billing address unless also providing a credit card.</td><td><p class="markdown-p">If you&#39;re creating a transaction using a credit card token, then we will use the billing address associated to that token in the Vault. You&#39;ll get this error if creating a transaction using a <a href="/reference/request/transaction/sale#payment_method_token">token</a> and specifying a <a href="/reference/request/transaction/sale#billing">billing address</a>.</p></td></tr>
    <tr id="code-91504" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91504</code></td><td>Transaction can only be voided if status is authorized, submitted_for_settlement, or - for PayPal - settlement_pending.</td><td><p class="markdown-p">Transaction can only be voided if status is authorized, submitted_for_settlement, or - for PayPal - settlement_pending.</p></td></tr>
    <tr id="code-91505" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91505</code></td><td>Credit transactions cannot be refunded.</td><td><p class="markdown-p">Only sale transactions can be refunded.</p></td></tr>
    <tr id="code-91506" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91506</code></td><td>Cannot refund a transaction unless it is settled.</td><td><p class="markdown-p">Transaction status must be settled to refund it.</p></td></tr>
    <tr id="code-91507" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91507</code></td><td>Cannot submit for settlement unless status is authorized.</td><td><p class="markdown-p">Transaction status must be authorized to submit the transaction for settlement.</p></td></tr>
    <tr id="code-91508" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91508</code></td><td>Cannot determine payment method.</td><td><p class="markdown-p">You must specify the payment method to charge, either directly (by payment_method_nonce, payment_method_token, credit_card, paypal_account, etc.) or indirectly (by customer_id, subscription_id, etc.).</p></td></tr>
    <tr id="code-91526" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91526</code></td><td>Custom field is invalid: </td><td><p class="markdown-p">Custom field keys must match the API name of a custom field configured in the Control Panel. The error message for this validation error will contain a list of the invalid keys.</p></td></tr>
    <tr id="code-91510" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91510</code></td><td>Customer ID is invalid.</td><td><p class="markdown-p">You&#39;ll get this error if you create a transaction using a customer ID and the customer ID isn&#39;t in your Vault.</p></td></tr>
    <tr id="code-91511" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91511</code></td><td>Customer does not have any credit cards.</td><td><p class="markdown-p">When creating a transaction using a customer ID, we&#39;ll use the customer&#39;s default credit card. If the customer does not have any credit cards associated to it, you&#39;ll get this error.</p></td></tr>
    <tr id="code-91512" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91512</code></td><td>Transaction has already been completely refunded.</td><td><p class="markdown-p">Transactions can only be refunded once.</p></td></tr>
    <tr id="code-91513" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91513</code></td><td>Merchant account ID is invalid.</td><td><p class="markdown-p">If you specify the merchant account ID to use to process a transaction and it does not match any of your merchant accounts, you&#39;ll get this error.</p></td></tr>
    <tr id="code-91514" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91514</code></td><td>Merchant account is suspended.</td><td><p class="markdown-p">You&#39;ll get this error if you try to create a transaction using a suspended merchant account.</p></td></tr>
    <tr id="code-91515" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91515</code></td><td>Cannot provide both payment_method_token and credit_card attributes.</td><td><p class="markdown-p">If you specify both a Vault token and a full credit card number you&#39;ll get this error.</p></td></tr>
    <tr id="code-91516" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91516</code></td><td>Cannot provide both payment_method_token and customer_id unless the payment_method belongs to the customer.</td><td><p class="markdown-p">If you specify both a customer ID and a payment method token when creating a transaction, the payment_method_token must belong to the customer ID.</p></td></tr>
    <tr id="code-91527" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91527</code></td><td>Cannot provide both payment_method_token and subscription_id unless the payment_method belongs to the subscription.</td><td><p class="markdown-p">If you specify both a payment method token and a subscription ID the subscription ID must be associated to the token given.</p></td></tr>
    <tr id="code-91517" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91517</code></td><td>Payment instrument type is not accepted by this merchant account.</td><td><p class="markdown-p">When providing a payment method token, your merchant account must be configured to accept the payment method type represented by the token.</p></td></tr>
    <tr id="code-91518" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91518</code></td><td>Payment method token is invalid.</td><td><p class="markdown-p">You&#39;ll get this error if the payment method token isn&#39;t in the Vault.</p></td></tr>
    <tr id="code-91519" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91519</code></td><td>Processor authorization code cannot be set unless for a voice authorization.</td><td><p class="markdown-p">You can only set the processor authorization code for voice authorization transactions.</p></td></tr>
    <tr id="code-91521" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91521</code></td><td>Refund amount is too large.</td><td><p class="markdown-p">You cannot refund more than the amount submitted for settlement.</p></td></tr>
    <tr id="code-91538" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91538</code></td><td>Cannot refund a transaction with a suspended merchant account.</td><td><p class="markdown-p">You cannot refund a transaction associated with a suspended merchant account.</p></td></tr>
    <tr id="code-91522" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91522</code></td><td>Settlement amount is too large.</td><td><p class="markdown-p">You can&#39;t settle more than the authorized amount unless your industry and processor support settlement adjustment (settling a certain percentage over the authorized amount); <a href="/forms/contact">contact our Accounts team</a> for details.</p></td></tr>
    <tr id="code-91529" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91529</code></td><td>Cannot provide both subscription_id and customer_id unless the subscription belongs to the customer.</td><td><p class="markdown-p">If you give both a customer ID and a subscription ID the subscription must be associated to the customer.</p></td></tr>
    <tr id="code-91528" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91528</code></td><td>Subscription ID is invalid.</td><td><p class="markdown-p">You&#39;ll get this error if the subscription ID given isn&#39;t one of your subscriptions.</p></td></tr>
    <tr id="code-91523" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91523</code></td><td>Transaction type is invalid.</td><td><p class="markdown-p">Valid transaction types are &quot;sale&quot; and &quot;credit&quot;.</p></td></tr>
    <tr id="code-91524" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91524</code></td><td>Transaction type is required.</td><td><p class="markdown-p">We need to know if you want to create a sale or a credit.</p></td></tr>
    <tr id="code-91525" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91525</code></td><td>Vault is disabled.</td><td><p class="markdown-p">If you set the option to store in Vault, your Vault needs to be enabled.</p></td></tr>
    <tr id="code-91531" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91531</code></td><td>Subscription status must be Past Due in order to retry.</td><td><p class="markdown-p">A subscription must be in past due status in order to manually retry the charge.</p></td></tr>
    <tr id="code-91547" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91547</code></td><td>Merchant account does not support refunds.</td><td><p class="markdown-p">The merchant account account does not support refunds.</p></td></tr>
    <tr id="code-81531" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81531</code></td><td>Amount must be greater than zero.</td><td><p class="markdown-p">The amount of a transaction cannot be zero.</p></td></tr>
    <tr id="code-81534" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81534</code></td><td>Tax amount cannot be negative.</td><td><p class="markdown-p">The tax amount cannot be less than zero.</p></td></tr>
    <tr id="code-81535" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81535</code></td><td>Tax amount is an invalid format.</td><td><p class="markdown-p">Tax amount must be formatted like &#39;10&#39; or &#39;10.00&#39;. If the <a href="/reference/general/currencies">currency does not use decimal places</a>, the amount cannot include decimal places.</p></td></tr>
    <tr id="code-81536" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81536</code></td><td>Tax amount is too large.</td><td><p class="markdown-p">The tax amount cannot be longer than 9 digits.</p></td></tr>
    <tr id="code-81571" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81571</code></td><td>Failed to authenticate, please try a different form of payment.</td><td><p class="markdown-p">Failed to authenticate, please try a different form of payment.</p></td></tr>
    <tr id="code-91537" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91537</code></td><td>Purchase order number is too long.</td><td><p class="markdown-p">The purchase order number cannot be larger than 12 characters for AIB and 17 characters for other all other processors.</p></td></tr>
    <tr id="code-91539" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91539</code></td><td>Voice Authorization is not allowed for this card type</td><td><p class="markdown-p">The specified card type does not support voice authorization codes.</p></td></tr>
    <tr id="code-91540" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91540</code></td><td>Transaction cannot be cloned if payment method is stored in vault.</td><td><p class="markdown-p">Instead, create a new transaction using the payment method&#39;s token.</p></td></tr>
    <tr id="code-91541" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91541</code></td><td>Cannot clone voice authorization transactions.</td><td><p class="markdown-p">Cloning voice authorizations is currently unsupported.</p></td></tr>
    <tr id="code-91542" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91542</code></td><td>Unsuccessful transaction cannot be cloned.</td><td><p class="markdown-p">Only transactions that were authorized or settled are cloneable.</p></td></tr>
    <tr id="code-91543" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91543</code></td><td>Credits cannot be cloned.</td><td><p class="markdown-p">You may only clone sale transactions.</p></td></tr>
    <tr id="code-91544" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91544</code></td><td>Cannot clone transaction without submit_for_settlement flag.</td><td><p class="markdown-p">You must specify whether or not to submit the cloned transaction for settlement upon creation.</p></td></tr>
    <tr id="code-91545" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91545</code></td><td>Voice Authorizations are not supported for this processor.</td><td><p class="markdown-p">Your processor does not support voice authorizations.</p></td></tr>
    <tr id="code-91546" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91546</code></td><td>Credits are not supported by this processor.</td><td><p class="markdown-p">Your processor does not support credits.</p></td></tr>
    <tr id="code-91548" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91548</code></td><td>Purchase order number is invalid.</td><td><p class="markdown-p">The purchase order number must be printable ASCII characters.</p></td></tr>
    <tr id="code-81520" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">81520</code></td><td>Processor authorization code must be 6 characters.</td><td><p class="markdown-p">Processor authorization code must be 6 characters.</p></td></tr>
    <tr id="code-91549" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91549</code></td><td>Cannot provide more than one of payment_method_token, payment_method_nonce, credit_card, and venmo_sdk_payment_method_code attributes.</td><td><p class="markdown-p">Cannot provide more than one of payment_method_token, payment_method_nonce, credit_card, and venmo_sdk_payment_method_code attributes.</p></td></tr>
    <tr id="code-91550" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91550</code></td><td>Channel is too long.</td><td><p class="markdown-p">Channel is too long. This field is for use by <strong>Partners and shopping cart providers only</strong>.</p></td></tr>
    <tr id="code-91551" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91551</code></td><td>Settlement amount cannot be less than the service fee amount.</td><td><p class="markdown-p">The settlement amount must be greater than or equal to the service fee amount.</p></td></tr>
    <tr id="code-91552" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91552</code></td><td>Credits not allowed with service fee.</td><td><p class="markdown-p">Service fees are allowed on sale transactions only.</p></td></tr>
    <tr id="code-91553" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91553</code></td><td>Sub-merchant account requires a service fee.</td><td><p class="markdown-p">Transactions for sub-merchant accounts need a service fee amount.</p></td></tr>
    <tr id="code-91554" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91554</code></td><td>Amount cannot be negative.</td><td><p class="markdown-p">Service fee amount must be greater than or equal to zero.</p></td></tr>
    <tr id="code-91555" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91555</code></td><td>Amount is an invalid format.</td><td><p class="markdown-p">Service fee amount must be formatted like &#39;10&#39; or &#39;10.00&#39;. If the <a href="/reference/general/currencies">currency does not use decimal places</a>, the amount cannot include decimal places.</p></td></tr>
    <tr id="code-91556" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91556</code></td><td>Service fee amount is larger than transaction amount.</td><td><p class="markdown-p">Service fee amount must be less than the transaction amount.</p></td></tr>
    <tr id="code-91557" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91557</code></td><td>Service fee not supported on master merchant account.</td><td><p class="markdown-p">Transactions for a master merchant account cannot have a service fee amount.</p></td></tr>
    <tr id="code-91558" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91558</code></td><td>Merchant account does not support MOTO transactions unless configured by processor.</td><td><p class="markdown-p">This merchant account cannot be used for Mail Order/Telephone Order.</p></td></tr>
    <tr id="code-91559" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91559</code></td><td>Cannot refund a transaction with a pending merchant account.</td><td><p class="markdown-p">A Merchant Account must be Active in order to refund a transaction.</p></td></tr>
    <tr id="code-91560" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91560</code></td><td>Transaction could not be held in escrow.</td><td><p class="markdown-p">The Transaction cannot be held in escrow.</p></td></tr>
    <tr id="code-91561" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91561</code></td><td>Cannot release a transaction that is not escrowed.</td><td><p class="markdown-p">Cannot release a transaction that is not escrowed.</p></td></tr>
    <tr id="code-91562" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91562</code></td><td>Release can only be cancelled if the transaction is submitted for release.</td><td><p class="markdown-p">Release can only be canceled if the transaction is submitted for release.</p></td></tr>
    <tr id="code-91563" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91563</code></td><td>Escrowed transactions cannot be partially refunded.</td><td><p class="markdown-p">The Transaction must be fully refunded after being held in escrow.</p></td></tr>
    <tr id="code-91564" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91564</code></td><td>Cannot use a payment_method_nonce more than once.</td><td><p class="markdown-p">The <a href="/guides/payment-method-nonces">payment method nonce</a> has already been consumed.</p></td></tr>
    <tr id="code-91565" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91565</code></td><td>Unknown or expired payment_method_nonce.</td><td><p class="markdown-p">The <a href="/guides/payment-method-nonces">payment method nonce</a> has either expired or never existed. Nonces are deleted upon expiration (3 hours after generation).</p></td></tr>
    <tr id="code-91567" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91567</code></td><td>Payment instrument type is not accepted by this merchant account.</td><td><p class="markdown-p">Payment instrument type is not accepted by this merchant account.</p></td></tr>
    <tr id="code-91568" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91568</code></td><td>Three D Secure Token is invalid.</td><td><p class="markdown-p">3D Secure token is invalid.</p></td></tr>
    <tr id="code-91569" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91569</code></td><td>payment_method_nonce does not contain a valid payment instrument type.</td><td><p class="markdown-p">payment_method_nonce does not contain a valid payment instrument type.</p></td></tr>
    <tr id="code-91572" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91572</code></td><td>Current payment method does not support use_billing_for_shipping flag.</td><td><p class="markdown-p">Current payment method does not support use_billing_for_shipping flag.</p></td></tr>
    <tr id="code-91575" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91575</code></td><td>Cannot transition transaction to settled, settlement_confirmed, or settlement_declined</td><td><p class="markdown-p">Cannot transition transaction to settled or settlement_declined.</p></td></tr>
    <tr id="code-91576" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91576</code></td><td>PayPal is not enabled for your merchant account.</td><td><p class="markdown-p">PayPal is not enabled for your merchant account.</p></td></tr>
    <tr id="code-91577" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91577</code></td><td>Merchant account does not support payment instrument.</td><td><p class="markdown-p">Merchant account does not support payment instrument.</p></td></tr>
    <tr id="code-91570" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91570</code></td><td>Transaction data does not match data from Three D Secure verify call.</td><td><p class="markdown-p">The credit card number and expiration date used for 3D Secure verification must match the values used to create the transaction.</p></td></tr>
    <tr id="code-91573" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91573</code></td><td>Transaction cannot be cloned if payment method is a PayPal account.</td><td><p class="markdown-p">Transaction cannot be cloned if payment method is a PayPal account.</p></td></tr>
    <tr id="code-91574" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91574</code></td><td>Cannot refund a transaction transaction in settling status on this merchant account. Try again after the transaction has settled.</td><td><p class="markdown-p">Cannot refund a transaction transaction in settling status on this merchant account. Try again after the transaction has settled.</p></td></tr>
    <tr id="code-91578" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91578</code></td><td>Service fee can not be applied on PayPal transactions.</td><td><p class="markdown-p">Service fee can not be applied on PayPal transactions.</p></td></tr>
    <tr id="code-91580" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91580</code></td><td>PayPal custom field must be less than 256 characters in length.</td><td><p class="markdown-p">PayPal custom field must be less than 256 characters in length.</p></td></tr>
    <tr id="code-91581" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91581</code></td><td>Shipping address customer does not match customer in request.</td><td><p class="markdown-p">Shipping address customer does not match customer in request.</p></td></tr>
    <tr id="code-91582" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91582</code></td><td>PayPal unilateral transactions must also be submitted for settlement.</td><td><p class="markdown-p">A unilateral payment is a payment that is made to a receiver who does not have a PayPal account.</p></td></tr>
    <tr id="code-91583" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91583</code></td><td>This PayPal account was not vaulted with the required data</td><td><p class="markdown-p">This PayPal account was not vaulted with the required data.</p></td></tr>
    <tr id="code-91584" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91584</code></td><td>Merchant account must match the 3D Secure authorization merchant account.</td><td><p class="markdown-p">The merchant account specified when creating the transaction must match the <a href="/guides/3d-secure/client-side#specify-a-merchant-account">merchant account specified when generating the client token</a>. If you do not specify a merchant account ID, your default merchant account will be used.</p></td></tr>
    <tr id="code-91585" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91585</code></td><td>Amount must match the 3D Secure authorization amount.</td><td><p class="markdown-p">The amount used for 3D Secure verification must match the amount used to create the transaction.</p></td></tr>
    <tr id="code-91586" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91586</code></td><td>Shared billing address ID cannot be used in the same call as a standard billing address ID</td><td><p class="markdown-p">Shared billing address ID cannot be used in the same call as a standard billing address ID.</p></td></tr>
    <tr id="code-91587" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91587</code></td><td>Shared customer ID cannot be used in the same call as a standard customer ID</td><td><p class="markdown-p">Shared customer ID cannot be used in the same call as a standard customer ID.</p></td></tr>
    <tr id="code-91588" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91588</code></td><td>Shared payment method token cannot be used in the same call as a standard payment method token</td><td><p class="markdown-p">Shared payment method token cannot be used in the same call as a standard payment method token.</p></td></tr>
    <tr id="code-91589" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91589</code></td><td>Shared payment method token cannot be used in the same call as a non-shared identifier param</td><td><p class="markdown-p">Shared payment method token cannot be used in the same call as a non-shared identifier param.</p></td></tr>
    <tr id="code-91590" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91590</code></td><td>Shared identifier param cannot be used with non-shared payment method token</td><td><p class="markdown-p">Shared identifier param cannot be used with non-shared payment method token.</p></td></tr>
    <tr id="code-91591" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91591</code></td><td>Shared shipping address ID cannot be used in the same call as a standard shipping address ID</td><td><p class="markdown-p">Shared shipping address ID cannot be used in the same call as a standard shipping address ID.</p></td></tr>
    <tr id="code-91592" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91592</code></td><td>Shared payment methods cannot be vaulted</td><td><p class="markdown-p">Shared payment methods cannot be vaulted.</p></td></tr>
    <tr id="code-91593" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91593</code></td><td>Shared payment methods cannot be vaulted</td><td><p class="markdown-p">Shared payment methods cannot be vaulted.</p></td></tr>
    <tr id="code-91594" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91594</code></td><td>Shared shipping addresses cannot be vaulted</td><td><p class="markdown-p">Shared shipping addresses cannot be vaulted.</p></td></tr>
    <tr id="code-91595" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91595</code></td><td>Shared payment methods cannot be updated</td><td><p class="markdown-p">Shared payment methods cannot be updated.</p></td></tr>
    <tr id="code-91597" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91597</code></td><td>Cannot provide both shared_payment_method_token and shared_customer_id unless the payment_method belongs to the customer.</td><td><p class="markdown-p">Cannot provide both shared_payment_method_token and shared_customer_id unless the payment_method belongs to the customer.</p></td></tr>
    <tr id="code-91598" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91598</code></td><td>Payment instrument type is not accepted by this merchant account.</td><td><p class="markdown-p">Payment instrument type is not accepted by this merchant account.</p></td></tr>
    <tr id="code-91599" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91599</code></td><td>Shared Shipping address customer does not match customer in request.</td><td><p class="markdown-p">Shared Shipping address customer does not match customer in request.</p></td></tr>
    <tr id="code-91596" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">91596</code></td><td>Shared payment method token is invalid.</td><td><p class="markdown-p">Shared payment method token is invalid.</p></td></tr>
    <tr id="code-915100" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915100</code></td><td>Shared Customer ID is invalid.</td><td><p class="markdown-p">Shared Customer ID is invalid.</p></td></tr>
    <tr id="code-915103" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915103</code></td><td>Cannot submit for partial settlement.</td><td><p class="markdown-p">Cannot submit for partial settlement.</p></td></tr>
    <tr id="code-915101" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915101</code></td><td>Payment instrument type is not accepted.</td><td><p class="markdown-p">Payment instrument type is not accepted.</p></td></tr>
    <tr id="code-915102" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915102</code></td><td>Partial settlements are not supported by this processor.</td><td><p class="markdown-p">Partial settlements are not supported by this processor.</p></td></tr>
    <tr id="code-915104" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915104</code></td><td>Delayed settlements are not supported for this processor. The submit for settlement option is required.</td><td><p class="markdown-p">Delayed settlements are not supported for this processor. The submit for settlement option is required.</p></td></tr>
    <tr id="code-915105" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915105</code></td><td>Merchant account does not support Amex rewards.</td><td><p class="markdown-p">Merchant account does not support Amex rewards.</p></td></tr>
    <tr id="code-915106" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915106</code></td><td>Points amount is too large.</td><td><p class="markdown-p">Amex Pay with Points amount is too large.</p></td></tr>
    <tr id="code-915152" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915152</code></td><td>request_id is required in a rewards payment request.</td><td><p class="markdown-p">request_id is required in a rewards payment request.</p></td></tr>
    <tr id="code-915153" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915153</code></td><td>points is required in a rewards payments required.</td><td><p class="markdown-p">points is required in a rewards payments required.</p></td></tr>
    <tr id="code-915154" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915154</code></td><td>currency_amount is required in a rewards payments required.</td><td><p class="markdown-p">currency_amount is required in a rewards payments required.</p></td></tr>
    <tr id="code-915155" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915155</code></td><td>currency_iso_code is required in a rewards payments required.</td><td><p class="markdown-p">currency_iso_code is required in a rewards payments required.</p></td></tr>
    <tr id="code-915107" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915107</code></td><td>Updating order_id on submit_for_settlement is not supported by this processor.</td><td><p class="markdown-p">Updating order_id on submit_for_settlement is not supported by this processor.</p></td></tr>
    <tr id="code-915108" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915108</code></td><td>Updating descriptor on submit_for_settlement is not supported by this processor.</td><td><p class="markdown-p">Updating descriptor on submit_for_settlement is not supported by this processor.</p></td></tr>
    <tr id="code-915109" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915109</code></td><td>PayPal supplementary data fields must be less than 4001 characters in length: </td><td><p class="markdown-p">PayPal supplementary data fields must be less than 4001 characters in length.</p></td></tr>
    <tr id="code-915110" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915110</code></td><td>Cannot clone facilitated transactions.</td><td><p class="markdown-p">Cannot clone facilitated transactions.</p></td></tr>
    <tr id="code-915111" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915111</code></td><td>PayPal supplementary data field count must be less than 101.</td><td><p class="markdown-p">PayPal supplementary data field count must be less than 101.</p></td></tr>
    <tr id="code-915112" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915112</code></td><td>Shared payment method token originated from another merchant and is not allowed to be shared</td><td><p class="markdown-p">Shared payment method token originated from another merchant and is not allowed to be shared.</p></td></tr>
    <tr id="code-915113" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915113</code></td><td>EciFlag is required.</td><td><p class="markdown-p">ECI flag is required for 3D Secure Pass Thru transactions.</p></td></tr>
    <tr id="code-915114" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915114</code></td><td>EciFlag is invalid.</td><td><p class="markdown-p">The provided ECI flag is invalid. Valid ECI Flags are: <ul><li>00</li><li>01</li><li>02</li><li>05</li><li>06</li><li>07</li></ul></p></td></tr>
    <tr id="code-915116" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915116</code></td><td>Cavv is required for specified EciFlag.</td><td><p class="markdown-p">CAVV is required for the specified ECI flag.</p></td></tr>





    <tr id="code-915131" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915131</code></td><td>Merchant account does not support 3D Secure transactions for card type.</td><td><p class="markdown-p">Merchant account has no active processor settings that support 3D Secure for this card type.</p></td></tr>
    <tr id="code-915156" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915156</code></td><td>Third party vault status must be either <code class="syntax-inline syntax-inline--theme">vaulted</code> or <code class="syntax-inline syntax-inline--theme">will_vault</code>.</td><td><p class="markdown-p">The vault status indicator passed with the transaction must be <code class="syntax-inline syntax-inline--theme">vaulted</code> or <code class="syntax-inline syntax-inline--theme">will_vault</code>.</p></td></tr>
    <tr id="code-915133" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915133</code></td><td>Transaction source must be either <code class="syntax-inline syntax-inline--theme">moto</code>, <code class="syntax-inline syntax-inline--theme">recurring_first</code>, <code class="syntax-inline syntax-inline--theme">recurring</code>, or <code class="syntax-inline syntax-inline--theme">merchant</code>.</td><td><p class="markdown-p">The ecommerce indicator (ECI) flag passed with the transaction must be <code class="syntax-inline syntax-inline--theme">moto</code>, <code class="syntax-inline syntax-inline--theme">recurring_first</code>, <code class="syntax-inline syntax-inline--theme">recurring</code>, or <code class="syntax-inline syntax-inline--theme">merchant</code>.</p></td></tr>
    <tr id="code-915134" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915134</code></td><td>submit_for_settlement is required and must be true.</td><td><p class="markdown-p">The payment method for this transaction does not support authorization with delayed settlement. Funds must be submitted for settlement upon creation.</p></td></tr>
    <tr id="code-915135" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915135</code></td><td>shared_payment_method_nonce does not contain valid payment instrument type.</td><td><p class="markdown-p">shared_payment_method_nonce does not contain valid payment instrument type.</p></td></tr>
    <tr id="code-915136" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915136</code></td><td>Payment instrument type is not accepted by this merchant.</td><td><p class="markdown-p">Payment instrument type is not accepted by this merchant.</p></td></tr>
    <tr id="code-915137" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915137</code></td><td>Cannot clone Braintree Marketplace transactions via the API.</td><td><p class="markdown-p">Braintree Marketplace transactions cannot be cloned via the API. If you wish to clone a Braintree Marketplace transaction, you must use the Braintree Control Panel.</p></td></tr>






    <tr id="code-915157" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915157</code></td><td>Too many line items.</td><td><p class="markdown-p">A maximum of 249 line items can be provided.</p></td></tr>
    <tr id="code-915158" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915158</code></td><td>Expected a collection of line items but none provided.</td><td><p class="markdown-p">Expected a collection of line items but unrecognized data provided.</p></td></tr>
    <tr id="code-915159" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915159</code></td><td>Discount amount is an invalid format.</td><td><p class="markdown-p">Discount amount must be formatted like &#39;10&#39; or &#39;10.00&#39;. If the <a href="/reference/general/currencies">currency does not use decimal places</a>, the amount can&#39;t include decimal places.</p></td></tr>
    <tr id="code-915160" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915160</code></td><td>Discount amount cannot be negative.</td><td><p class="markdown-p">Discount amount can&#39;t be less than zero.</p></td></tr>
    <tr id="code-915161" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915161</code></td><td>Discount amount is too large.</td><td><p class="markdown-p">Discount amount can&#39;t be longer than 9 digits.</p></td></tr>
    <tr id="code-915162" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915162</code></td><td>Shipping amount is an invalid format.</td><td><p class="markdown-p">Shipping amount must be formatted like &#39;10&#39; or &#39;10.00&#39;. If the <a href="/reference/general/currencies">currency does not use decimal places</a>, the amount can&#39;t include decimal places.</p></td></tr>
    <tr id="code-915163" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915163</code></td><td>Shipping amount cannot be negative.</td><td><p class="markdown-p">Shipping amount can&#39;t be less than zero.</p></td></tr>
    <tr id="code-915164" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915164</code></td><td>Shipping amount is too large.</td><td><p class="markdown-p">Shipping amount can&#39;t be longer than 9 digits.</p></td></tr>
    <tr id="code-915165" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915165</code></td><td>Ships from postal code is too long.</td><td><p class="markdown-p">Ships from postal code must not contain more than 9 letters and numbers.</p></td></tr>
    <tr id="code-915166" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915166</code></td><td>Ships from postal code must be a string.</td><td><p class="markdown-p">Ships from postal code must be a string.</p></td></tr>
    <tr id="code-915167" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915167</code></td><td>Ships from Postal code can only contain letters, numbers, spaces, and hyphens.</td><td><p class="markdown-p">Ships from Postal code can only contain letters, numbers, spaces, and hyphens.</p></td></tr>


    <tr id="code-915147" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915147</code></td><td>Vaulted cards from this payment method can only be used for recurring transactions.</td><td><p class="markdown-p">This payment method only allows recurring transactions from vaulted cards. All other transactions are not allowed with vaulted cards.</p></td></tr>
    <tr id="code-915148" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915148</code></td><td>Transaction can not be voided if status of a PayPal partial settlement child transaction is settlement_pending.</td><td><p class="markdown-p">Transaction can not be voided if status of a PayPal partial settlement child transaction is settlement_pending.</p></td></tr>
    <tr id="code-915149" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915149</code></td><td>Too many concurrent attempts to refund this transaction. Try again later.</td><td><p class="markdown-p">Too many concurrent attempts to refund this transaction. Try again later.</p></td></tr>

    <tr id="code-915151" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915151</code></td><td>Too many concurrent attempts to void this transaction. Try again later.</td><td><p class="markdown-p">Too many concurrent attempts to void this transaction. Try again later.</p></td></tr>
    <tr id="code-915168" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915168</code></td><td>Device session id must be less than 256 characters.</td><td><p class="markdown-p">The device session id provided is too long. It must be less than 256 characters.</p></td></tr>
    <tr id="code-915169" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915169</code></td><td>Merchant account does not support 3D Secure.</td><td><p class="markdown-p">The transacting merchant account must be configured to support 3D Secure. Either <a href="/reference/request/transaction/sale#specify-merchant-account">specify a merchant account</a> that has 3D Secure enabled, or <a href="/forms/contact">contact our Support team</a>.</p></td></tr>
    <tr id="code-915170" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915170</code></td><td>Venmo Profile ID does not exist.</td><td><p class="markdown-p">The Venmo Profile associated with the <code class="syntax-inline syntax-inline--theme">profile_id</code> does not exist.</p></td></tr>
    <tr id="code-915171" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915171</code></td><td>US bank account payment_method_nonce must originate from Plaid or be vaulted prior to transaction.</td><td><p class="markdown-p">US bank accounts must be verified before they can be charged. This can be done by either tokenizing with Plaid or vaulting the nonce and providing verification options.</p></td></tr>
    <tr id="code-915172" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">915172</code></td><td>US bank account payment method must be verified prior to transaction.</td><td><p class="markdown-p">US bank accounts must be verified before they can be charged. This can be done by updating the payment method and providing verification options.</p></td></tr>
  </tbody>
</table>

<h3 class="markdown-h3">
  Authorization Adjustment
  <a class="icon icon--link hash-link" href="#authorization-adjustment">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="authorization-adjustment"></a>
</h3>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-95601" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95601</code></td><td>Transaction must be submitted for settlement for the authorized amount.</td><td><p class="markdown-p">Transaction cannot be adjusted and must be submitted for settlement for the authorized amount.</p></td></tr>
    <tr id="code-95602" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95602</code></td><td>Failed to submit for settlement for an amount different than the authorized amount. Please submit for the authorized amount.</td><td><p class="markdown-p">By submitting an amount other than the authorized amount, an adjustment needed to be performed on the transaction. This adjustment resulted in a hard decline and should not be retried.</p></td></tr>
    <tr id="code-95603" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95603</code></td><td>Failed to submit for settlement for an amount different than the authorized amount. Please try again at a later time.</td><td><p class="markdown-p">By submitting an amount other than the authorized amount, an adjustment needed to be performed on the transaction. This adjustment resulted in a soft decline and can be retried.</p></td></tr>
    <tr id="code-95604" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95604</code></td><td>Failed to submit for settlement for an amount different than the authorized amount too many times. Please submit for the authorized amount.</td><td><p class="markdown-p"><strong>Deprecated</strong><br/> By submitting an amount other than the authorized amount, an adjustment needed to be performed on the transaction. This adjustment has resulted in too many failures. Please try again later or submit for the authorized amount.</p></td></tr>
  </tbody>
</table>

<h3 class="markdown-h3">
  Descriptor
  <a class="icon icon--link hash-link" href="#descriptor">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="descriptor"></a>
</h3>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-92201" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92201</code></td><td>Company name/DBA section is invalid.</td><td><p class="markdown-p">The company/DBA name passed in your <a href="/reference/request/transaction/sale#descriptor">descriptor</a> does not meet the requirements set by your processor.</p></td></tr>
    <tr id="code-92202" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92202</code></td><td>Phone number is invalid.</td><td><p class="markdown-p">Typically, phone must be 10 - 14 characters and can only contain numbers, dashes, parentheses and periods. Some example phone numbers are:</p>
<ul class="list list--disc"><li>3125556666</li>
<li>312-555-6666</li>
<li>(312)555-6666<br></li>
</ul>
<p class="markdown-p">However, your processor may impact the number of characters or format accepted. <a href="/forms/contact">Contact Support</a> for more information on your processor&#39;s specific requirements.</p></td></tr>
    <tr id="code-92203" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92203</code></td><td>Dynamic descriptors have not been enabled for this account. Please contact support at <a href="https://developers.braintreepayments.com/forms/contact">https://developers.braintreepayments.com/forms/contact</a>.</td><td><p class="markdown-p">Dynamic descriptors have not been enabled for this account. <a href="/forms/contact">Contact our Support team</a>.</p></td></tr>
    <tr id="code-92204" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92204</code></td><td>Descriptor format is invalid.</td><td><p class="markdown-p">Descriptor name must be less than or equal to 15 characters and can only contain letters and numbers. This will be prefixed by the preset company name for this account.</p></td></tr>
    <tr id="code-92205" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92205</code></td><td>International phone number is invalid.</td><td><p class="markdown-p"><strong>Deprecated</strong><br/> Phone can only contain numbers, dashes and periods and must be less than or equal to 13 characters.</p></td></tr>
    <tr id="code-92206" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">92206</code></td><td>URL must be 13 characters or shorter.</td><td><p class="markdown-p">The url/web address to a customer&#39;s statement must be less than or equal to 13 characters.</p></td></tr>
  </tbody>
</table>

<h3 class="markdown-h3">
  Transaction Line Items
  <a class="icon icon--link hash-link" href="#transaction-line-items">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="transaction-line-items"></a>
</h3>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-95801" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95801</code></td><td>Commodity code is too long.</td><td><p class="markdown-p">Commodity code can&#39;t be longer than 12 characters.</p></td></tr>
    <tr id="code-95803" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95803</code></td><td>Description is too long.</td><td><p class="markdown-p">Description can&#39;t be longer than 127 characters.</p></td></tr>
    <tr id="code-95804" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95804</code></td><td>Discount amount is an invalid format.</td><td><p class="markdown-p">Discount amount must be formatted like &#39;10&#39; or &#39;10.00&#39;. If the <a href="/reference/general/currencies">currency does not use decimal places</a>, the amount can&#39;t include decimal places.</p></td></tr>
    <tr id="code-95805" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95805</code></td><td>Discount amount is too large.</td><td><p class="markdown-p">Discount amount is too large.</p></td></tr>
    <tr id="code-95806" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95806</code></td><td>Discount amount cannot be negative.</td><td><p class="markdown-p">Discount amount can&#39;t be less than zero.</p></td></tr>
    <tr id="code-95807" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95807</code></td><td>Kind must be &#39;debit&#39; or &#39;credit&#39;.</td><td><p class="markdown-p">Kind must be &#39;debit&#39; or &#39;credit&#39;.</p></td></tr>
    <tr id="code-95808" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95808</code></td><td>Kind is required.</td><td><p class="markdown-p">Kind is required, and must be &#39;debit&#39; or &#39;credit&#39;.</p></td></tr>
    <tr id="code-95809" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95809</code></td><td>Product code is too long.</td><td><p class="markdown-p">Product code can&#39;t be longer than 12 characters, or 127 characters for PayPal transactions.</p></td></tr>
    <tr id="code-95810" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95810</code></td><td>Quantity is in an invalid format.</td><td><p class="markdown-p">Quantity must be formatted like &#39;10&#39; or &#39;10.0000&#39;.</p></td></tr>
    <tr id="code-95811" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95811</code></td><td>Quantity is required.</td><td><p class="markdown-p">Quantity is required.</p></td></tr>
    <tr id="code-95812" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95812</code></td><td>Quantity is too large.</td><td><p class="markdown-p">Quantity can&#39;t be longer than 12 digits.</p></td></tr>
    <tr id="code-95813" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95813</code></td><td>Total amount is an invalid format.</td><td><p class="markdown-p">Total amount must be formatted like &#39;10&#39; or &#39;10.00&#39;. If the <a href="/reference/general/currencies">currency does not use decimal places</a>, the amount can&#39;t include decimal places.</p></td></tr>
    <tr id="code-95814" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95814</code></td><td>Total amount is required.</td><td><p class="markdown-p">Total amount is required.</p></td></tr>
    <tr id="code-95815" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95815</code></td><td>Total amount is too large.</td><td><p class="markdown-p">Total amount can&#39;t be longer than 9 digits.</p></td></tr>
    <tr id="code-95816" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95816</code></td><td>Total amount must be greater than zero.</td><td><p class="markdown-p">Total amount can&#39;t be less than zero.</p></td></tr>
    <tr id="code-95817" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95817</code></td><td>Unit amount is an invalid format.</td><td><p class="markdown-p">Unit amount must be formatted like &#39;10&#39; or &#39;10.0000&#39;.</p></td></tr>
    <tr id="code-95818" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95818</code></td><td>Unit amount is required.</td><td><p class="markdown-p">Unit amount is required.</p></td></tr>
    <tr id="code-95819" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95819</code></td><td>Unit amount is too large.</td><td><p class="markdown-p">Unit amount can&#39;t be longer than 12 digits.</p></td></tr>
    <tr id="code-95820" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95820</code></td><td>Unit amount must be greater than zero.</td><td><p class="markdown-p">Unit amount can&#39;t be less than or equal to zero.</p></td></tr>
    <tr id="code-95821" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95821</code></td><td>Unit of measure is too long.</td><td><p class="markdown-p">Unit of measure cannot be longer than 12 characters.</p></td></tr>
    <tr id="code-95822" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95822</code></td><td>Name is required.</td><td><p class="markdown-p">Name is required.</p></td></tr>
    <tr id="code-95823" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95823</code></td><td>Name is too long.</td><td><p class="markdown-p">Maximum 35 characters or 127 characters for PayPal transactions.</p></td></tr>
    <tr id="code-95824" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95824</code></td><td>Unit tax amount is an invalid format.</td><td><p class="markdown-p">Unit tax amount must be formatted like &#39;10&#39; or &#39;10.00&#39;. If the <a href="/reference/general/currencies">currency does not use decimal places</a>, the unit tax amount can&#39;t include decimal places.</p></td></tr>
    <tr id="code-95825" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95825</code></td><td>Unit tax amount is too large.</td><td><p class="markdown-p">Unit tax amount is too large.</p></td></tr>
    <tr id="code-95826" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95826</code></td><td>Unit tax amount cannot be negative.</td><td><p class="markdown-p">Unit tax amount can&#39;t be less than or equal to zero.</p></td></tr>
    <tr id="code-95827" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95827</code></td><td>Tax amount is an invalid format.</td><td><p class="markdown-p">Tax amount must be formatted like &#39;10&#39; or &#39;10.00&#39;. If the <a href="/reference/general/currencies">currency does not use decimal places</a>, the unit tax amount can&#39;t include decimal places.</p></td></tr>
    <tr id="code-95828" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95828</code></td><td>Tax amount is too large.</td><td><p class="markdown-p">Tax amount can&#39;t be longer than 9 digits.</p></td></tr>
    <tr id="code-95829" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">95829</code></td><td>Tax amount cannot be negative.</td><td><p class="markdown-p">Tax amount can&#39;t be less than zero.</p></td></tr>
  </tbody>
</table>

<h2 class="markdown-h2">
  Verification
  <a class="icon icon--link hash-link" href="#verification">
    <svg class="icon--svg icon--link" viewBox="0 0 27 29" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
      <path d="M16.1743,11.8514 L17.9143,10.1114 C16.5073,8.7054 14.8473,7.9414 12.9323,7.8184 C11.0163,7.6954 9.3733,8.3014 8.0023,9.6364 L1.8343,15.8054 C0.4993,17.1754 -0.1077,18.8194 0.0153,20.7344 C0.1383,22.6504 0.9033,24.3194 2.3093,25.7434 C3.7153,27.1654 5.3753,27.9304 7.2913,28.0364 C9.2063,28.1414 10.8493,27.5434 12.2203,26.2444 L14.1183,24.2924 L12.4313,22.5534 L10.4803,24.5034 C9.7423,25.2774 8.7323,25.6284 7.4493,25.5584 C6.1663,25.4884 5.0323,24.9694 4.0493,24.0024 C3.0643,23.0364 2.5373,21.9124 2.4673,20.6284 C2.3973,19.3464 2.7653,18.3184 3.5743,17.5444 L9.7423,11.3764 C10.4803,10.5684 11.4903,10.1994 12.7743,10.2694 C14.0563,10.3394 15.1903,10.8674 16.1743,11.8514 M10.6383,16.1734 L8.8993,17.9134 C10.3043,19.3204 11.9653,20.0834 13.8813,20.2064 C15.7963,20.3304 17.4393,19.7414 18.8103,18.4414 L24.9783,12.2204 C26.3143,10.8494 26.9203,9.2054 26.7973,7.2904 C26.6743,5.3754 25.9093,3.7144 24.5043,2.3084 C23.0983,0.9034 21.4373,0.1384 19.5223,0.0154 C17.6063,-0.1076 15.9633,0.4984 14.5923,1.8344 L13.0633,3.3104 L14.8033,5.0504 L16.3323,3.5744 C17.0703,2.7654 18.0813,2.3964 19.3633,2.4664 C20.6463,2.5374 21.7793,3.0644 22.7643,4.0484 C23.7483,5.0334 24.2753,6.1654 24.3453,7.4494 C24.4163,8.7324 24.0473,9.7424 23.2383,10.4804 L17.0703,16.7014 C16.3323,17.4744 15.3213,17.8264 14.0393,17.7554 C12.7563,17.6854 11.6223,17.1584 10.6383,16.1734" fill-rule="evenodd"/>
      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link.png">
    </svg>
  </a>
  <a class="hash-link-target" name="verification"></a>
</h2>
<table class="table--selectable-rows">
  <thead>
    <tr>
      <th>Code</th>
      <th>Text</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr id="code-94201" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">94201</code></td><td>Verification amount cannot be negative.</td><td><p class="markdown-p">Verification amount cannot be negative.</p></td></tr>
    <tr id="code-94202" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">94202</code></td><td>Verification amount is invalid.</td><td><p class="markdown-p">Verification amount is invalid.</p></td></tr>
    <tr id="code-94203" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">94203</code></td><td>Verification amount not supported by processor.</td><td><p class="markdown-p">Verification amount not supported by processor.</p></td></tr>
    <tr id="code-94204" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">94204</code></td><td>Verification Merchant Account ID is invalid.</td><td><p class="markdown-p">Verification Merchant Account ID is invalid.</p></td></tr>
    <tr id="code-94205" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">94205</code></td><td>Verification Merchant Account is suspended.</td><td><p class="markdown-p">Verification Merchant Account is suspended.</p></td></tr>
    <tr id="code-94206" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">94206</code></td><td>The current user does not have access to the specified merchant_account_id</td><td><p class="markdown-p">The current user does not have access to the specified merchant_account_id.</p></td></tr>
    <tr id="code-94207" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">94207</code></td><td>Verification amount is too large.</td><td><p class="markdown-p">Verification amount is too large.</p></td></tr>
    <tr id="code-94208" class="selectable-row"><td><code class="syntax-inline syntax-inline--theme">94208</code></td><td>Verification Merchant Account ID cannot be a sub-merchant account.</td><td><p class="markdown-p">Verifications cannot be created using sub-merchant accounts.</p></td></tr>
  </tbody>
</table>



      
          <div class="section-wrapper">
            <div class="section section--centered section--vertical section--separated">
              <span class="section__articles-graphic">
                <svg viewBox="0 0 204 36" class="icon--svg icon--lifesaver" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
                  <g fill-rule="evenodd">
                    <path d="M18,35 L18,35 C27.3888407,35 35,27.3888407 35,18 C35,8.61115925 27.3888407,1 18,1 C8.61115925,1 1,8.61115925 1,18 C1,27.3888407 8.61115925,35 18,35 L18,35 Z M18,36 L18,36 C8.0588745,36 0,27.9411255 0,18 C0,8.0588745 8.0588745,0 18,0 C27.9411255,0 36,8.0588745 36,18 C36,27.9411255 27.9411255,36 18,36 L18,36 Z M18,27 L18,27 C22.9705627,27 27,22.9705627 27,18 C27,13.0294373 22.9705627,9 18,9 C13.0294373,9 9,13.0294373 9,18 C9,22.9705627 13.0294373,27 18,27 L18,27 Z M18,28 L18,28 C12.4771525,28 8,23.5228475 8,18 C8,12.4771525 12.4771525,8 18,8 C23.5228475,8 28,12.4771525 28,18 C28,23.5228475 23.5228475,28 18,28 L18,28 Z" transform="translate(84)"/>
                    <path d="M8.93879849 22.2358226L1 24C.336844422 22.117617 0 20.0994429 0 18 0 15.9005571.336844422 13.882383 1 12L8.93879849 13.7641774C8.3365015 15.0503868 8 16.4858963 8 18 8 19.5141037 8.3365015 20.9496132 8.93879849 22.2358226L8.93879849 22.2358226zM27.0612015 22.2358226L35 24C35.6631556 22.117617 36 20.0994429 36 18 36 15.9005571 35.6631556 13.882383 35 12L27.0612015 13.7641774C27.6634985 15.0503868 28 16.4858963 28 18 28 19.5141037 27.6634985 20.9496132 27.0612015 22.2358226L27.0612015 22.2358226zM22.3408367 27.0112763L24 35.0422485C22.117617 35.6631556 20.0994429 36 18 36 15.9005571 36 13.882383 35.6631556 12 35.0422485L12 35.0422485 13.6591633 27.0112763C14.97206 27.6448731 16.4445578 28 18 28 19.5554422 28 21.02794 27.6448731 22.3408367 27.0112763L22.3408367 27.0112763zM22.3408367 8.98872372L24 .957751542C22.117617.336844422 20.0994429 0 18 0 15.9005571 0 13.882383.336844422 12 .957751542L12 .957751542 13.6591633 8.98872372C14.97206 8.35512686 16.4445578 8 18 8 19.5554422 8 21.02794 8.35512686 22.3408367 8.98872372L22.3408367 8.98872372zM6.76462838 3.93620125L5.24612202 2.41769489C4.46401367 1.63558655 3.19526215 1.63316498 2.41421356 2.41421356 1.62771965 3.20070747 1.63472362 4.46315075 2.41769489 5.24612202L3.93620125 6.76462838C4.77142532 5.72050597 5.72050597 4.77142532 6.76462838 3.93620125L6.76462838 3.93620125 6.76462838 3.93620125zM7.47173516 3.22909447L7.47173516 3.22909447 8.26179511 4.01915443 7.38928974 4.71709701C6.40285655 5.50617378 5.50617378 6.40285655 4.71709701 7.38928974L4.01915443 8.26179511 3.22909447 7.47173516 1.71058811 5.9532288C.536010671 4.77865136.531156209 2.88305735 1.70710678 1.70710678 2.87883893.535374634 4.78075312.538112437 5.9532288 1.71058811L7.47173516 3.22909447zM3.91007061 29.2026278L2.41769489 30.6950035C1.63472362 31.4779747 1.62771965 32.740418 2.41421356 33.5269119 3.19526215 34.3079605 4.46401367 34.305539 5.24612202 33.5234306L6.73195354 32.0375991C5.68981562 31.1999976 4.74291633 30.2487355 3.91007061 29.2026278L3.91007061 29.2026278 3.91007061 29.2026278zM3.20296383 28.495521L3.20296383 28.495521 3.99486757 27.7036172 4.69241126 28.579777C5.47919868 29.5680326 6.3738102 30.4667865 7.35842154 31.258152L8.22728184 31.9564843 7.43906032 32.7447059 5.9532288 34.2305374C4.78075312 35.4030131 2.87883893 35.4057509 1.70710678 34.2340187.531156209 33.0580681.536010671 31.1624741 1.71058811 29.9878967L3.20296383 28.495521zM29.2353716 32.0637987L30.6950035 33.5234306C31.4771118 34.305539 32.7458634 34.3079605 33.5269119 33.5269119 34.3134058 32.740418 34.3064019 31.4779747 33.5234306 30.6950035L32.0637987 29.2353716C31.2285747 30.279494 30.279494 31.2285747 29.2353716 32.0637987L29.2353716 32.0637987 29.2353716 32.0637987zM28.5282648 32.7709055L28.5282648 32.7709055 27.7382049 31.9808456 28.6107103 31.282903C29.5971434 30.4938262 30.4938262 29.5971434 31.282903 28.6107103L31.9808456 27.7382049 32.7709055 28.5282648 34.2305374 29.9878967C35.4051148 31.1624741 35.4099693 33.0580681 34.2340187 34.2340187 33.0622866 35.4057509 31.1603724 35.4030131 29.9878967 34.2305374L28.5282648 32.7709055zM32.0375991 6.73195354L33.5234306 5.24612202C34.3064019 4.46315075 34.3134058 3.20070747 33.5269119 2.41421356 32.7458634 1.63316498 31.4771118 1.63558655 30.6950035 2.41769489L29.2026278 3.91007061C30.2487355 4.74291633 31.1999976 5.68981562 32.0375991 6.73195354L32.0375991 6.73195354 32.0375991 6.73195354zM32.7447059 7.43906032L32.7447059 7.43906032 31.9564843 8.22728184 31.258152 7.35842154C30.4667865 6.3738102 29.5680326 5.47919868 28.579777 4.69241126L27.7036172 3.99486757 28.495521 3.20296383 29.9878967 1.71058811C31.1603724.538112437 33.0622866.535374634 34.2340187 1.70710678 35.4099693 2.88305735 35.4051148 4.77865136 34.2305374 5.9532288L32.7447059 7.43906032z" transform="translate(84)"/>
                    <path d="M1 15.5C4.57885136 15.5 6.34129723 16.2149882 9.59394139 18.4142067 12.9967972 20.7149882 14.9318514 21.5 18.748 21.5 22.5639677 21.5 24.4991001 20.7150125 27.9017978 18.4144675 27.9019853 18.4143408 27.9019853 18.4143408 27.9021728 18.414214 31.1549126 16.2150547 32.9177013 15.5 36.497 15.5 40.0761137 15.5 41.8388551 16.2149765 45.0917239 18.4139751 45.0919114 18.4141019 45.0919114 18.4141019 45.0920989 18.4142286 48.4954176 20.7149342 50.4310191 21.5 54.248 21.5 58.0649809 21.5 60.0005824 20.7149342 63.4039011 18.4142286 63.4040886 18.4141019 63.4040886 18.4141019 63.4042761 18.4139751 66.6571449 16.2149765 68.4198863 15.5 71.999 15.5 72.2751424 15.5 72.499 15.2761424 72.499 15 72.499 14.7238576 72.2751424 14.5 71.999 14.5 68.1826276 14.5 66.2472926 15.2849813 62.8442239 17.5855178 62.8440364 17.5856446 62.8440364 17.5856446 62.8438489 17.5857714 59.5907301 19.784939 57.8277274 20.5 54.248 20.5 50.6682726 20.5 48.9052699 19.784939 45.6521511 17.5857714 45.6519636 17.5856446 45.6519636 17.5856446 45.6517761 17.5855178 42.2487074 15.2849813 40.3133724 14.5 36.497 14.5 32.6804237 14.5 30.7450249 15.285072 27.3420772 17.585786 27.3418897 17.5859128 27.3418897 17.5859128 27.3417022 17.5860395 24.0892124 19.7850298 22.326685 20.5 18.748 20.5 15.1691486 20.5 13.4067028 19.7850118 10.1540586 17.5857933 6.75120277 15.2850118 4.81614864 14.5 1 14.5.723857625 14.5.5 14.7238576.5 15 .5 15.2761424.723857625 15.5 1 15.5L1 15.5zM132 15.5C135.578851 15.5 137.341297 16.2149882 140.593941 18.4142067 143.996797 20.7149882 145.931851 21.5 149.748 21.5 153.563968 21.5 155.4991 20.7150125 158.901798 18.4144675 158.901985 18.4143408 158.901985 18.4143408 158.902173 18.414214 162.154913 16.2150547 163.917701 15.5 167.497 15.5 171.076114 15.5 172.838855 16.2149765 176.091724 18.4139751 176.091911 18.4141019 176.091911 18.4141019 176.092099 18.4142286 179.495418 20.7149342 181.431019 21.5 185.248 21.5 189.064981 21.5 191.000582 20.7149342 194.403901 18.4142286 194.404089 18.4141019 194.404089 18.4141019 194.404276 18.4139751 197.657145 16.2149765 199.419886 15.5 202.999 15.5 203.275142 15.5 203.499 15.2761424 203.499 15 203.499 14.7238576 203.275142 14.5 202.999 14.5 199.182628 14.5 197.247293 15.2849813 193.844224 17.5855178 193.844036 17.5856446 193.844036 17.5856446 193.843849 17.5857714 190.59073 19.784939 188.827727 20.5 185.248 20.5 181.668273 20.5 179.90527 19.784939 176.652151 17.5857714 176.651964 17.5856446 176.651964 17.5856446 176.651776 17.5855178 173.248707 15.2849813 171.313372 14.5 167.497 14.5 163.680424 14.5 161.745025 15.285072 158.342077 17.585786 158.34189 17.5859128 158.34189 17.5859128 158.341702 17.5860395 155.089212 19.7850298 153.326685 20.5 149.748 20.5 146.169149 20.5 144.406703 19.7850118 141.154059 17.5857933 137.751203 15.2850118 135.816149 14.5 132 14.5 131.723858 14.5 131.5 14.7238576 131.5 15 131.5 15.2761424 131.723858 15.5 132 15.5L132 15.5z"/>
                  </g>
                </svg>
              </span>
              <h3 class="section__title">Still have questions?</h3>
                <p class="section__description">If you can’t find an answer,
                  <a class="section__link icon is-external-link docs-link" href="/forms/contact" target="_blank" data-track-event-properties="project=journey,action=click,type=link,descriptor=page support contact">
                    contact our Support team<svg class="icon--svg icon--link--external icon--link--external--inline" viewBox="0 0 15 15" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
                      <title>External link icon</title>
                      <g fill-rule="evenodd">
                        <path d="M0 -0.0003L0 14.9997 15 14.9997 15 9.4757 13.235 9.4757 13.235 13.2347 1.765 13.2347 1.765 1.7647 5.524 1.7647 5.524 -0.0003z"/>
                        <path d="M8.685 -0.0003L8.685 1.7647 11.938 1.7647 4.579 9.1227 5.828 10.3717 13.235 2.9627 13.235 6.3137 15 6.3137 15 -0.0003z"/>
                      </g>
                      <image class="icon--fallback" xlink:href="" src="img/fallback/icon--link--external.png">
                    </svg>
                  </a>
                </p>
            </div>
          </div>
            <div class="section--feedback">
              <a class="button button--secondary" id='feedback-link' href="https://docs.google.com/forms/d/1vjNpzXbgr7l646hb039dj5V33HjBTPLPhmx-zhWvIaA/viewform?entry.1171727737=" data-track-event-properties="project=journey,action=click,type=link,descriptor=page feedback">Give us some feedback on this page</a>
            </div>
    </article>
    <footer class="footer wrap nocontent">
      <ul class="footer-link-list" data-track-event-properties="project=journey,action=click,type=link,descriptor=footer">
        <li><a class="footer__link" href="https://braintreepayments.com" data-track-event-properties="project=journey,action=click,type=link,descriptor=footer marketing site">&larr; Braintreepayments.com</a></li>
        <li class="text-light">|</li>
        <li><a class="footer__link" href="https://developers.braintreepayments.com" target="_blank">Developer Docs</a></li>
        <li><a class="footer__link" href="https://articles.braintreepayments.com" target="_blank" data-track-event-properties="project=journey,action=click,type=link,descriptor=footer articles">Support Articles</a></li>
        <li><a class="footer__link" href="https://status.braintreepayments.com" target="_blank" data-track-event-properties="project=journey,action=click,type=link,descriptor=footer status">Status</a></li>
      </ul>
      <div class="legal">
      &copy; 2008-2018 Braintree, a service of PayPal, Inc. All rights reserved. <a href="https://www.paypal.com/us/webapps/mpp/ua/privacy-full">Privacy Policy</a> | <a href="https://braintreepayments.com/legal">Legal</a>
      </div>
    </footer>
  </div>
</div>

         
    </div>
  </div>

    <script>
    window.emulateArticlesSubdomain = false;
    window.env = "production";
    window.isArticles = false;
    window.isStagingOrProduction = true;
    </script>
    
    <input type="hidden" name="_csrf" value="">
    <script src="/js/app.built.js?4735cf8cfa73c7de6513366cef0034697f6014ee"></script>
    
    <script>
      ga('create', 'UA-1885256-2', 'auto', {
        'allowLinker': true
      });
      ga('require', 'displayfeatures');
      ga('send', 'pageview');
    </script>
    
    <!-- start Google Tag Manager -->
    <script>
    dataLayer = [{
    'gtm.blacklist': ['nonGoogleScripts', 'nonGoogleIframes']
    }];
    </script>
    <noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM­P2QMX6" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start': new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-P2QMX6');</script>
    <!-- end Google Tag Manager -->
    
    <!-- start Mixpanel -->
    <script type="text/javascript">
    if (mixpanel != null) {
      mixpanel.init("57d5c7e8c26326eea294e689d752d4e2", {'cross_subdomain_cookie': true, 'cookie_name': 'docs_mixpanel'});
      mixpanel.init("539f4132fec85ce346b6f7f99cb7614e", {'cross_subdomain_cookie': true, 'cookie_name': 'b_journey'}, 'journey');
      mixpanel.track('pageview', {'Endpoint': window.location.pathname});
      mixpanel.journey.track('pageview', {'Endpoint': window.location.pathname, 'origin': 'b_docs'});
    }
    </script>
    <!-- end Mixpanel -->
    
    <!-- start Eloqua -->
    <script type="text/javascript">
      var _elqQ = _elqQ || [];
      _elqQ.push(['elqSetSiteId', '94483084']);
      _elqQ.push(['elqTrackPageView']);
      (function () {
        function async_load() {
          var s = document.createElement('script'); s.type = 'text/javascript'; s.async = true;
          s.src = '//img.en25.com/i/elqCfg.min.js';
          var x = document.getElementsByTagName('script')[0]; x.parentNode.insertBefore(s, x);
        }
        if (window.addEventListener) window.addEventListener('DOMContentLoaded', async_load, false);
        else if (window.attachEvent) window.attachEvent('onload', async_load);
      })();
    </script>
    <!-- end Eloqua -->
    
    <script type="text/javascript">
      // For additional SVG's this should be abstracted
      var ajax = new XMLHttpRequest();
      ajax.open("GET", "/img/svg/diagrams.svg", true);
      ajax.send();
      ajax.onload = function(e) {
        var div = document.createElement("div");
        div.classList.add('hide');
        div.innerHTML = ajax.responseText;
        document.body.insertBefore(div, document.body.childNodes[0]);
      }
    </script>

  <script>
    function goBack() {
      window.history.back()
    }
  </script>
  </body>
</html>
```

matchObj = re.match(r'.*code-(d{5})', text);
if(matchObj)
    print matchObj.group()                                                                                                                                    
            
