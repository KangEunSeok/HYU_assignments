import React from 'react';
import { Route } from 'react-router-dom';
import { connect } from 'react-redux';
import { setMobileNavVisibility } from '../../reducers/Layout';
import { withRouter } from 'react-router-dom';

import Header from './Header';
import LoginHeader from './LoginHeader'
import AdminHeader from './AdminHeader'
import SideBar from '../../components/SideBar';
import AdminSideBar from '../../components/AdminSideBar'
/**
 * Pages
 */
import Components from '../Components';
import UserProfile from '../UserProfile';
import Forms from '../Forms';
import Tables from '../Tables';
import test from '../test';
import Login from '../Login';
import Signup from '../Signup';
import Event from '../Event';
import ApplyPart from '../ApplyPart'
import ApplyVol from '../ApplyVol'
import ApplyedEvents from '../ApplyedEvents'
import ApplyedPart from '../ApplyedPart'
import ApplyedVol from '../ApplyedVol'
import manager_ManageEvent from '../manager_ManageEvent'
import manager_event from '../manager_event'
import manager_UploadEvent from '../manager_UploadEvent'
import manager_ModifyEvent from '../manager_ModifyEvent'
import EditProfile from '../EditProfile'
import FindIdPw from '../FindIdPw'

const Main = ({
  mobileNavVisibility,
  hideMobileMenu,
  history
}) => {
  history.listen(() => {
    if (mobileNavVisibility === true) {
      hideMobileMenu();
    }
  });
  console.log(history.location.pathname)
    
  if (history.location.pathname==='/' || history.location.pathname==='/Signup'|| history.location.pathname==='/FindIdPw'){
    return(
      <div className="wrapper">
        <div className="main-panel">
          <LoginHeader />
          <Route exact path="/" component={Login} />
          <Route path="/Signup" component={Signup} />
          <Route path="/FindIdPw" component={FindIdPw} />
        </div>
      </div>

    )
  }else if(history.location.pathname==='/manager_ManageEvent'|| history.location.pathname==='/manager_event' || history.location.pathname==='/manager_UploadEvent' || history.location.pathname==='/manager_ModifyEvent'){
    return(
        <div className="wrapper">
          <AdminSideBar />
          <div className="main-panel">
            <AdminHeader />
            <Route exact path="/manager_ManageEvent" component={manager_ManageEvent} />
            <Route path="/manager_event" component={manager_event}/>
            <Route path="/manager_UploadEvent" component={manager_UploadEvent} />
            <Route path="/manager_ModifyEvent" component={manager_ModifyEvent} />
          </div>
        </div>
      )
  }
  else{
    return(
        <div className="wrapper">
          <SideBar />
          <div className="main-panel">
            <Header />
            <Route exact path="/test" component={test} />
            <Route path="/Event" component={Event} />
            <Route path="/EditProfile" component={EditProfile} />
            <Route path="/ApplyPart" component={ApplyPart} />
            <Route path="/ApplyVol" component={ApplyVol} />
            <Route path="/ApplyedEvents" component={ApplyedEvents} />
            <Route path="/ApplyedVol" component={ApplyedVol}/>
            <Route path="/ApplyedPart" component={ApplyedPart}/>
            <Route path="/components" component={Components} />
            <Route path="/profile" component={UserProfile} />
            <Route path="/forms" component={Forms} />
            <Route path="/tables" component={Tables} />
          </div>
        </div>
    )
  }
  
};

const mapStateToProp = state => ({
  mobileNavVisibility: state.Layout.mobileNavVisibility
});

const mapDispatchToProps = (dispatch, ownProps) => ({
  hideMobileMenu: () => dispatch(setMobileNavVisibility(false))
});

export default withRouter(connect(mapStateToProp, mapDispatchToProps)(Main));