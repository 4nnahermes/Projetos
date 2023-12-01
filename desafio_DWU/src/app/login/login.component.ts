import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  usuario: string = '';
  senha: string = '';

  constructor(private router: Router) {}

  login(): void {
    if (this.usuario === 'DWU' && this.senha === 'DWU2023') {
      this.router.navigate(['/formulario']);
    } else {
      alert('Credenciais inválidas');
    }
  }
}

