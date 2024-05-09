package entidades;

public class Data {
    private int dia;
    private int mes;
    private int ano;


    public Data(int dia, int mes, int ano) {
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
    }

    public int getDia() {
        return dia;
    }
    public int getMes() {
        return mes;
    }
    public int getAno() {
        return ano;
    }

    public void escreverAData() {
        System.out.printf("Data: %d/%d/%d", dia, mes, ano);
    }
}
