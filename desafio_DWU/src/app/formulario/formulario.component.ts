import { Component } from '@angular/core';

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.css'],
})
export class FormularioComponent {
  formulario = {
    nome: '',
    sobrenome: '',
    idade: 0,
    sexo: 'N',
    dataNascimento: '',
  };

  formularioEnviado = false;

  salvarDados(): void {
    this.formularioEnviado = true;

    if (this.formularioValido()) {
      console.log(this.formulario);
      this.formulario = {
        nome: '',
        sobrenome: '',
        idade: 0,
        sexo: 'N',
        dataNascimento: '',
      };
      alert('Dados salvos com sucesso!');
    } else {
      alert('Por favor, preencha todos os campos.');
    }
  }

  formularioValido(): boolean {
    return (
      this.formulario.nome !== '' &&
      this.formulario.sobrenome !== '' &&
      this.formulario.idade > 0 &&
      this.formulario.sexo !== 'N' &&
      this.formulario.dataNascimento !== ''
    );
  }
}
