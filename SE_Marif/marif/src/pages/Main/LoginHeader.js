import React from 'react';
import { connect } from 'react-redux';
import { toggleMobileNavVisibility } from '../../reducers/Layout';
import { Navbar, Nav, NavItem} from 'react-bootstrap';

const LoginHeader = ({
  showMobileMenu,
  toggleMobileNavVisibility
}) => (
    <Navbar fluid={true}>
      <Navbar.Collapse>
        <div className="separator"></div>
        <Nav>
          <NavItem> MALIF - 유기견 산책 행사 </NavItem>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );

const mapDispatchToProp = dispatch => ({
  toggleMobileNavVisibility: () => dispatch(toggleMobileNavVisibility())
});

export default connect(null, mapDispatchToProp)(LoginHeader);