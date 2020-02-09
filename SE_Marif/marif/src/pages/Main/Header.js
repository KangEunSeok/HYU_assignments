import React from 'react';
import { connect } from 'react-redux';
import { toggleMobileNavVisibility } from '../../reducers/Layout';
import { Navbar, Nav, NavItem} from 'react-bootstrap';
import { Link } from 'react-router-dom';


const Header = ({
  showMobileMenu,
  toggleMobileNavVisibility
}) => (
    <Navbar fluid={true}>
      <Navbar.Collapse>
        <div className="separator"></div>
        <Nav>
          <NavItem> MALIF - 유기견 산책 행사 </NavItem>
        </Nav>
        <Nav pullRight> 
          <NavItem>
            <Link to="/">
              Log out
            </Link>
          </NavItem>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );

const mapDispatchToProp = dispatch => ({
  toggleMobileNavVisibility: () => dispatch(toggleMobileNavVisibility())
});

export default connect(null, mapDispatchToProp)(Header);